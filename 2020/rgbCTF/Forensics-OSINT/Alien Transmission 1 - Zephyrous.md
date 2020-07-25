# rgbCTF - Alien Transmission 1

**Category:** Forensics/OSINT
**Points:** 500 initial, 219 final
**Solves:** 158, 64th to solve

> I was listening to my radio the other day and received this strange message... I think it came from an alien?
>
> squeakymusic.wav

*Writeup by:* Dan Walter (Zephyrous)

## Process

This one was a very simple SSTV signal. The only messing around with it that I had to do was to resample the .wav file we were given from 44.1KHz to 11.025KHz, because that’s the sample rate that my SSTV decoder likes to be fed (I use MMSSTTV). 

Formatted correctly, MMSSTV decodes it to the following:

![MMSSTV Output](https://raw.githubusercontent.com/swin-scsc/writeups/orangeblossomest-uploading-1/2020/rgbCTF/Forensics-OSINT/images/alien_transmission_1-zephyrous-screenshot.png)

### Flag: rgbCTF{s10w_2c4n_1s_7h3_W4V3}
