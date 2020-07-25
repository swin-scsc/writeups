# rgbCTF - Advanced Reversing Mechanics 1

**Category:** Pwn/Rev
**Points:** 500 initial, 216 final
**Solves:** 159, 156th to solve

> Very very advanced trust me
>
> 71, 66, 61, 42, 53, 45, 7A, 40, 51, 4C, 5E, 30, 79, 5E, 31, 5E, 64, 59, 5E, 38, 61, 36, 65, 37, 63, 7C,
>
> - arm_easy.o

*Writeup by:* Dan Walter (Zephyrous)

## Process

This one was fairly simple, but had a twist thrown in. There was also a file given, but it was about as useless as a turning indicator in a BMW.

We were given a string of hex digits (see the description), that when converted from hex to ascii, spat out the following: `qfaBSEz@QL^0y^1^dY^8a6e7c|`. At first glance, this looked like gibberish, but the first 6 characters gave it away – three lowercase, three uppercase, which was the flag format (rgbCTF). This then required rot-47 (as oppose to rot-13) with a rotation amount of 1, which then gave me the flag.
### Flag: rgbCTF{ARM_1z_2_eZ_9b7f8d}
