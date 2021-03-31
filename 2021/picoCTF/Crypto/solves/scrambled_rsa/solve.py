import telnetlib
from string import printable

tn = telnetlib.Telnet('mercury.picoctf.net', 58251)

response = tn.read_until(b'me: ').split(b'\n')
flag = response[0].split(b': ')[1]

known = b''
cts = []
printable = [a.encode() for a in printable[0:printable.index('}') + 1]]

def remove_knowns(res, cts):
    for ct in cts:
        if ct in res:
            idx = res.index(ct)
            res = res[:idx] + res[idx + len(ct):]
    return res

# Try until last char is '}' (125)
while known == b'' or known[-1] != 125:
    found = False
    
    # Write and read all at once as it's faster
    tn.write(b'\n'.join([known + char for char in printable]) + b'\n')

    for char in printable:
        tn.read_until(b': ')
        ct = remove_knowns(tn.read_until(b': ').split(b'\n')[0], cts)
        if not found and ct in flag:
            cts.append(ct)
            known += char
            # Cannot break here as we still need to read stuff from socket
            found = True
            print(known)
