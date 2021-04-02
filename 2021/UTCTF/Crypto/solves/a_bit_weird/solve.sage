from Crypto.Util.number import long_to_bytes as l2b

with open('msg.txt') as f:
    N = int(f.readline().split('= ')[1].replace('\n', ''))
    e = int(f.readline().split('= ')[1].replace('\n', ''))
    c = int(f.readline().split('= ')[1].replace('\n', ''))
    _and = int(f.readline().split('= ')[1].replace('\n', ''))
    f.readline()
    x = int(f.readline().split('= ')[1].replace('\n', ''))

bl = int(_and).bit_length()
bl += int(8 - bl % 8)

xx = (x >> bl) * 2 ** bl
a1 = xx ** 3
a2 = (3 * xx ** 2) % N
a3 = (3 * xx) % N
z = (c - a1) % N

PR.<y> = PolynomialRing(Zmod(N))
f = a2 * y + a3 * y ** 2 + y ** 3 - z
root = f.small_roots(X=2 ** bl)

_or = int(xx + int(root[0]))
and_bits = bin(_and)[2:].zfill(bl)
or_bits = bin(_or % 2 ** bl)[2:].zfill(bl)
x_bits = bin(x % 2 ** bl)[2:].zfill(bl)

o = ''

for i in range(bl):
    if or_bits[i] == '0':
        o += '0'
    elif x_bits[i] == '0':
        o += '1'
    else:
        o += and_bits[i]

print(l2b(int(o, 2)))
