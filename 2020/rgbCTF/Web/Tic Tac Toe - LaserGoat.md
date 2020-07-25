# rgbCTF - Tic Tac Toe

**Category:** Web 
**Points:** 50
**Solves:** 333

> Hello there, I invite you to one of the largest online global events in history ... the Tic Tac Toe World Championships!
>
> http://challenge.rgbsec.xyz:8974/

*Writeup By:* Lukas (LaserGoat)

## Solution:

This was quite a simple challenge. Upon opening the URL provided, we found a 3x3 grid in which you can play Tic Tac Toe against a CPU player. 

![Tic Tac Toe Screenshot](https://raw.githubusercontent.com/swin-scsc/writeups/master/2020/rgbCTF/Web/images/tic_tac_toe-lasergoat-screenshot-1.png)

When you lose, no flag is given (obviously).

![Tic Tac Toe Loss Screenshot](https://raw.githubusercontent.com/swin-scsc/writeups/master/2020/rgbCTF/Web/images/tic_tac_toe-lasergoat-screenshot-2.png)

If the game ends in a draw, you are rewarded with a flag! Too bad it’s invalid.

![Tic Tac Toe Draw Screenshot](https://raw.githubusercontent.com/swin-scsc/writeups/master/2020/rgbCTF/Web/images/tic_tac_toe-lasergoat-screenshot-3.png)

Upon winning against the CPU, we are finally rewarded the flag.


### Flag: rgbCTF{h4h4_j4v42cr1p7_ev3n72_AR3_c00L}
