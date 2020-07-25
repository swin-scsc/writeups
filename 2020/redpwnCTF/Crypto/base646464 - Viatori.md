# redpwnCTF - Base646464

**Category:** Crypto
**Points:** 145 
**Solves:** 1023

> Encoding something multiple times makes it exponentially more secure!
>
> - Files: generate.js, cipher.txt

*Writeup By:* Viatori

## Process:

First thing I do is take a look at the ciphertext. It looks like base64, unsurprisingly. I open the program used to encode it, and note that the method is run 25 times. Rather than modify the program, I elected to use CyberChef to decode the ciphertext.

### Flag: flag{l00ks_l1ke_a_l0t_of_64s}

