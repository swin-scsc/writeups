from Crypto.Util.number import bytes_to_long as b2l, long_to_bytes as l2b
from Crypto.Random.random import randint
from Crypto.Util.number import inverse
from itertools import product
from pwn import *

ROUNDS = 5
BLOCK_LEN = 8

def pad(p):
    if len(p) % BLOCK_LEN != 0:
        return p + b'\x00' * (BLOCK_LEN - (len(p) % BLOCK_LEN))
    else:
        return p

def g(i):
    b = bin(i).lstrip('0b').rstrip('L').rjust(BLOCK_LEN * 8, '0')
    return int(b[::-1], 2)

def encrypt_block(b, k):
    result = b2l(b)
    for i in range(ROUNDS):
        key = b2l(k[i * BLOCK_LEN:(i + 1) * BLOCK_LEN])
        key_odd = key | 1
        result ^= key
        result = g(result)
        result = (result * key_odd) % (1 << 64)
    return hex(result).lstrip('0x').rstrip('L').zfill(BLOCK_LEN * 2)

def encrypt(msg, k):
    plain = pad(msg)
    result = ""
    for i in range(0, len(plain), BLOCK_LEN):
        result += encrypt_block(plain[i:i + BLOCK_LEN], k)
    return result

def decrypt_block(b, k):
    result = b2l(b)
    for i in range(ROUNDS - 1, -1, -1):
        key = b2l(k[i * BLOCK_LEN:(i + 1) * BLOCK_LEN])
        key_odd = key | 1
        result = result * pow(key_odd, -1, 2 ** 64) % 2 ** 64
        result = g(result)
        result ^= key
    return hex(result).lstrip('0x').rstrip('L').zfill(BLOCK_LEN * 2)

def decrypt(msg, k):
    result = ''
    for i in range(0, len(msg), BLOCK_LEN):
        result += decrypt_block(msg[i:i + BLOCK_LEN], k)
    return result

# Condition 1 from Furman's paper
def condition1(a, b):
    # 10 must be the LSBs of the XOR difference,
    # and 0 must be the LSB of each plaintext 
    return (a ^ b) % 4 == 2 and a % 2 == 0 and b % 2 == 0

def store(notes):
    payload = b''

    for note in notes: payload += b'1\n' + note + b'\n'

    p.send(payload)
   
    for _ in notes: p.recvuntil(b'? ')

def retrieve(idx, num_notes):
    payload = b''
    out = []
    
    for i in range(num_notes):
        payload += b'2' + b'\n' + str(i + idx).encode() + b'\n'

    p.send(payload)
    p.recvuntil(b'? ')
    
    for i in range(num_notes):
        out.append(p.recvuntil(b'\n').strip()[-16:].decode())
        p.recvuntil(b'?')

    return out

def flatten(a):
    return [b for _ in a for b in _]

#p = process('./p.py')
p = remote('mercury.picoctf.net', 10304)

p.recvuntil(b'? ')
p.sendline(b'2')
p.recvuntil(b'? ')
p.sendline(b'0')
res = p.recvuntil(b'\n')
p.recvuntil(b'? ')

flag_ciphertext = bytes.fromhex(res[:-1].decode())

word_size = 2 ** 64
diff = 2 ** 63 - 2
inv = inverse(diff, word_size)

def find_subkeys(ciphertexts):
    subkeys = []

    for pair in ciphertexts:
        if condition1(pair[0], pair[1]):
            s = pair[0] + pair[1]
            if s % 2 == 0:
                subkeys.append((inv * s % word_size) // 2 % word_size)
    
    most_common_subkey = max(set(subkeys), key=subkeys.count)
    
    # Return 4 subkeys, one flipped MSBs and LSBs
    return (most_common_subkey, most_common_subkey ^ 2 ** 63,
            most_common_subkey ^ 1, most_common_subkey ^ 2 ** 63 ^ 1)

# Basically reversing one round
def partially_decrypt(ciphertext, subkey):
    plaintext = ciphertext * inverse(subkey, word_size) % word_size
    plaintext = g(plaintext)
    return plaintext ^ subkey

def crack_round(partially_decrypted):
    subkey1, subkey2, subkey3, subkey4 = find_subkeys(partially_decrypted)
    next_partially_decrypted1 = [(partially_decrypt(a[0], subkey1),
                                  partially_decrypt(a[1], subkey1))
                                  for a in partially_decrypted]
    next_partially_decrypted2 = [(partially_decrypt(a[0], subkey2),
                                  partially_decrypt(a[1], subkey2))
                                  for a in partially_decrypted]
    next_partially_decrypted3 = [(a ^ 1, b ^ 1)
                                 for a, b in next_partially_decrypted1]
    next_partially_decrypted4 = [(a ^ 1, b ^ 1)
                                 for a, b in next_partially_decrypted2]
    return ([next_partially_decrypted1, next_partially_decrypted2,
            next_partially_decrypted3, next_partially_decrypted4],
            [subkey1, subkey2, subkey3, subkey4])

def _filter(arr, minimum):
    return [a for a in arr
            if len([b for b in a
                    if b[0] ^ b[1] == diff]) >= minimum]
nn = 0
idx = 1

while True:
    plaintexts = []

    for i in range(32):
        plaintext1 = randint(0, 2 ** 63 - 1) & word_size - 2
        plaintext2 = plaintext1 ^ diff
        plaintexts.append((plaintext1, plaintext2))
        plaintexts.append((plaintext1 ^ 2 ** 63, plaintext2 ^ 2 ** 63))


    flattened = flatten(plaintexts)
    num_notes = len(flattened)

    store([hex(a)[2:].zfill(16).encode() for a in flattened])
    responses = retrieve(idx, num_notes)
    idx += num_notes

    ciphertexts = [(int(responses[i], 16), int(responses[i + 1], 16))
                   for i in range(0, len(responses) - 1, 2)]

    cand_keys = [[] for _ in range(5)]

    partially_decrypted_values, subkeys = crack_round(ciphertexts)
    cand_keys[0] = subkeys

    minim = len([pair for pair in ciphertexts
                 if pair[0] ^ pair[1] == diff])

    for i in range(4):
        minim = 2 * minim + 2
        next_partially_decrypted_values = []

        for partially_decrypted in partially_decrypted_values:
            next_partially_decrypted, subkeys = crack_round(partially_decrypted)
            cand_keys[i + 1] += subkeys
            next_partially_decrypted_values += next_partially_decrypted
    
        partially_decrypted_values = _filter(next_partially_decrypted_values,
                                             minim)

    k1s, k2s, k3s, k4s, k5s = [list(set(cand_keys[i])) for i in range(4, -1, -1)]
    nn = len(k1s) * len(k2s) * len(k3s) * len(k4s) * len(k5s)

    if nn == 0 or nn > 2 ** 18:
        print(f"{nn} combinations is no good! Trying again...")
        continue

    combs = product(k1s, k2s, k3s, k4s, k5s)

    for comb in combs:
        k = b''.join([l2b(cc).rjust(8, b'\x00') for cc in comb])
        encrypted = [encrypt(l2b(plaintexts[i][0]), k) for i in range(4)]
       
        # Assert that the key is good for 4 plaintexts 
        if all([int(encrypted[i], 16) == ciphertexts[i][0] for i in range(4)]):
            print(bytes.fromhex(decrypt(flag_ciphertext, k)))

    break
