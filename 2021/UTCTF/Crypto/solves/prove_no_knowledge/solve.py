import telnetlib

tn = telnetlib.Telnet('crypto.utctf.live', 4354)

res = tn.read_until(b'mod p.\n')
p = int(str(res).split('p: ')[1].split('y:')[0][:-2])
y = int(str(res).split('y: ')[1][:-37])

x1 = b'0'
x2 = b'1'
x3 = str(pow(y, -1, p)).encode()
x4 = b'0'

payload = b''

for i in range(256):
    if i % 2 == 0:
        payload += x2 + b'\n' + x1 + b'\n'
    else:
        payload += x3 + b'\n' + x4 + b'\n'
    
tn.write(payload)

for i in range(511): tn.read_until(b'.\n')

print(tn.read_until(b'.\n'))
