import telnetlib

tn = telnetlib.Telnet('crypto.utctf.live', 4354)

res = tn.read_until(b'mod p.\n')
p = int(str(res).split('p: ')[1].split('y:')[0][:-2])
y = int(str(res).split('y: ')[1][:-37])

x1 = 0
x2 = 1
x3 = pow(y, -1, p)
x4 = 0

for i in range(256):
    if i % 2 == 0:
        tn.write((str(x2) + '\n').encode())
    else:
        tn.write((str(x3) + '\n').encode())
    print(tn.read_until(b'.\n'))
    
    if i % 2 == 0:
        tn.write((str(x1) + '\n').encode())
    else:
        tn.write((str(x4) + '\n').encode())
    print(tn.read_until(b'.\n'))
