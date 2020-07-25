# rgbCTF - Lo-Fi
**Category:** Forensics/OSINT
**Points:** 500 initial, 499 final
**Solves:** 7, 2nd to solve

> I made a "inspirational" lo-fi track! ft. Alec's very smooth aussie accent. 
>
> You know, "Just do it", "Don't let your dreams be ones and zeroes", I'm pretty sure he says something along those lines... all inspirational sayings mean the same thing anyway.
>
> - lofi.wav

*Writeup by:* Dan Walter (Zephyrous)

## Process

Lo-fi was a song written that had binary data encoded into the lead synth riff, and them some spectrographic data encoded right after that. That riff sounded like this, and the spectrographic view of the entire file looked like this:

- lofi_banger.mp3

![lofi_banger.mp3 Spectographic View](https://raw.githubusercontent.com/swin-scsc/writeups/master/2020/rgbCTF/Forensics-OSINT/images/lofi-zephyrous-screenshot-1.png)

Resising those short beeps immediately succeeding the synth lead is the word TINYURL. 

![lofi_banger.mp3 Spectographic View Resized](https://raw.githubusercontent.com/swin-scsc/writeups/master/2020/rgbCTF/Forensics-OSINT/images/lofi-zephyrous-screenshot-2.png)

This meant that I was looking for a string of characters that would make up the “random” aspect of a tinyurl link – tinyurl.com/xxxxxxx. At this point, probably because I work a bit with electronic music and DAWs (digital audio workstations) mainly for fun, I already knew exactly where the data to be decoded was, I just had to figure out how. As to where and how the data was encoded, it was in the synth keys. I highly suggest giving a listen to the song if you haven’t already.

I was trying to determine if it had something to do with the distance between the hits, or when they were in the file, but what made the most sense was simply binary – a synth hit for a 1, and no syth hit for a 0. So I cleaned up the file – I removed the bass, the drum and the kick using some audio editing, and was left with this:

- lofi_clean.mp3

From this point on, I was more interested with the waveform, rather than the spectrographic view:

![lofi_clean.mp3 Waveform](https://raw.githubusercontent.com/swin-scsc/writeups/master/2020/rgbCTF/Forensics-OSINT/images/lofi-zephyrous-screenshot-3.png)

I still had the problem of trying to figure out some kind of a line this up to a timeline, but I figured that I could use *itself* as a timeline. I threw it into my photo editor, made a copy of the waveform, turned it red, and floated it up a bit.

![lofi_clean.mp3 Waveform 2](https://raw.githubusercontent.com/swin-scsc/writeups/master/2020/rgbCTF/Forensics-OSINT/images/lofi-zephyrous-screenshot-4.png)

From here I could make copies of the red waveform, shift them either left or right, and line up the peaks.

![lofi_clean.mp3 Waveform 3](https://raw.githubusercontent.com/swin-scsc/writeups/master/2020/rgbCTF/Forensics-OSINT/images/lofi-zephyrous-screenshot-5.png)

![lofi_clean.mp3 Waveform 4](https://raw.githubusercontent.com/swin-scsc/writeups/master/2020/rgbCTF/Forensics-OSINT/images/lofi-zephyrous-screenshot-6.png)

From here, it was a fairly simple job of interpreting this into binary bits. Essentially, you’re running an AND operation on each peak of the red waveform and what was directly below it, which looks like this:

![lofi_clean.mp3 Waveform Binary](https://raw.githubusercontent.com/swin-scsc/writeups/master/2020/rgbCTF/Forensics-OSINT/images/lofi-zephyrous-screenshot-7.png)

That gives us the string 011001100110101000101101001100110011000000110010, which when converted to ascii gives us ‘fj-302’, which would mean the tinyurl link is tinyurl.com/fj-302, which takes us to a pastebin, where we get our flag:

### Flag: rgbCTF{subscr1b3_t0_qu1nt3c_0n_yt_plz}
