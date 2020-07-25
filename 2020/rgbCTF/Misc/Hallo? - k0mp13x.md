# rgbCTF - Hallo? 
**Category:** Misc
**Points:** 50
**Solved:** #63

> The flag is exactly as decoded. No curly brackets.
> 
> NOTE: keep the pound symbols as pound symbols!
>
> - hmm.mp3
*Writeup by:* k0mp13x

## Process

Tools:
https://onlinetonegenerator.com/dtmf.html
https://tino1b2be.github.io/DTMF-Decoder/    

Solve:

The tones are DTMF tones. I started manually decoding the tones using reference tones. This was taking a bit long, so I found a DTMF decoder online and sent the file to it.

The output:

7774222228333#99933338#386333#866666337777#

Then I broke this up into the groupings that match the waveform output to get the breakup of numbers.

777 4 22 222 8 333 # 999 33 33 8 # 3 8 6 333 # 8 666 66 33 7777 #

![Phone Keypad](https://raw.githubusercontent.com/swin-scsc/writeups/master/2020/rgbCTF/Misc/images/hallo-k0mp13x-screenshot.png)

The numbers correspond to a phone keypad.

### Flag: rgbCTF#yeet#dtmf#tones#
