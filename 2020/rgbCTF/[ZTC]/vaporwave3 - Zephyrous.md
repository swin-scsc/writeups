# rgbCTF - vaporwave3

**Category:** [ZTC]
**Points:** 500 initial, 496 final
**Solves:** 19, 3rd to solve

> Hone your skills, find new strategies, get your time splits down, and maybe you can claim the new Ninja Gaiden, Wii Sports Resort Golf, or Blindfolded Punch-Out world record speedrun!
>
> - chall.zip

*Writeup by:* Dan Walter (Zephyrous)

## Process:
This challenge gave us 8 different .mp3 files with unique, hashed names, that were UUIDs. In each file’s spectrographic display, there were three characters, here is the view of a randomly picked one of the eight: 

![Spectrographic Display Screenshot](https://raw.githubusercontent.com/swin-scsc/writeups/master/2020/rgbCTF/%5BZTC%5D/images/vaporwave3-zeph-screenshot.png)

Copying down these characters, and arranging them by song length, longest to shortest, gives us janOHS{ahse0n1yz_k4f73p}. This is obviously the correct first step, but there’s more to read here than meets the eye.
Firstly, “janOHS{xxxxxxxxx_xxxxxx}” gives us four pieces of crucial information.

1.  “janOHS” will probably be decoded somehow into rgbCTF.
2.  that this is encoded as a cipher – it is encoded alphabetically in nature.
3.  that however this is encoded does not take into account if a character is uppercase or lowercase, that is to say, if it is uppercase, it stays that way when encoded or decoded, and vise-versa.
4.  the presence of the curly bracket and underscore implies that however this is encoded can not deal with symbols, and probably for that matter (when point 2 is considered) numbers either.

Upon considering the cipher that could be at play here, I immediately settled on a vigenere cipher. So using dcode’s vigenere cipher tool (https://www.dcode.fr/vigenere-cipher) I entered in the flag janOHS{ahse0n1yz_k4f73p} and selected “Knowing a plaintext word”, which in this case was “rgbCTF”.

That gave me a partial key of “SUMMON”, and using that key gave me rgbCTF{ings0z1lh_q4t73d}. This however, was still incorrect. I re-read the challenge description and entered “summon” alongside ninja gaiden – which gave me a youtube video by someone called “Summoning Salt” on the history of ninja gaiden world records. Doing the same thing for Wii Sports Resort Golf gave me a Summoning Salt video, too. 100 point to anyone who can guess who made a video about the history of Blindfold Punchout, too.

So I entered ‘SUMMONING SALT’ as the vigenere cipher key, and it gave me the flag.

### Flag: rgbCTF{summ0n1ng_s4l73d}
