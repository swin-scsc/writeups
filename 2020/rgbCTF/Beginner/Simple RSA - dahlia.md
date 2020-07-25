# rgbCTF - Simple RSA

**Category:** Beginner 
**Points:**  50/500
**Solves:** 228/436

> Can you find a way to attack this RSA implementation?
> 
> Hint! What's the simplest attack against RSA?
> 
> ~qpwoeirut#5057
> 
> - simple_rsa.txt
>   - Size: 0.12 KB
>   - MD5: 890e58f8d143ee2e7f761779500b591f
> - simple_rsa.py
>   - Size: 0.39 KB
>   - MD5: 292f34897f99b5b4178cadca1a725b80

*Writeup By:* [dahlia](https://github.com/orangeblossomest)

# Solution

With this challenge we were given two files simple_rsa.txt, a text file containing the n, e and c values for an RSA encryption:

```
n = 5620911691885906751399467870749963159674169260381
e = 65537
c = 1415060907955076984980255543080831671725408472748
```

and simple_rsa.py, containing an RSA encryption algorithm:

```python
from sympy import randprime, mod_inverse
from math import gcd

def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)

p = randprime(1e40, 1e41)
q = randprime(1e8, 1e9)
e = 65537

n = p * q

lmbd = lcm(p - 1, q - 1)
d = mod_inverse(e, lmbd)

message = b"REDACTED"
m = int.from_bytes(message, 'little')
c = pow(m, e, n)

assert pow(c, d, n) == m

print("n =", n)
print("e =", e)
print("c =", c)
```

This challenge was a very simple one, as the modulus n had such a small value that it was easy to determine its prime factors. I used https://www.alpertron.com.ar/ECM.HTM to get the the values of p and q

`5 620911 691885 906751 399467 870749 963159 674169 260381 (49 digits) = 255 097177 × 22034 393943 473183 756163 118460 342519 430053 (41 digits)`

This site is also useful as in its output it provides euler's totient (phi = (p-1)*(q-1)), which is required to determine the private exponent d, used for decryption:

`5 620911 669851 512807 926284 114586 844699 331394 733152`

I used these values:

```
phi = 5620911669851512807926284114586844699331394733152
n = 5620911691885906751399467870749963159674169260381
e = 65537
c = 1415060907955076984980255543080831671725408472748
```

as input for a RSA solver python script, which was able to determine d using phi and e, and thus decrypt c to gave me the flag:

### Flag: rgbCTF{brut3_f0rc3}






