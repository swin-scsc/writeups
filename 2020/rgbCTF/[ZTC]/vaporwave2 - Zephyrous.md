# rgbCTF - vaporwave2
**Category:** [ZTC]
**Points:** 500 initial, 462 final
**Solves:** 58, 14th to solve
> I got two versions. I got twooo versions…
>
> - vaporwave2a.flac
> - vaporwave2b.flac


*Writeup by:* Dan Walter (Zephyrous)
## Process
The challenge included two audio files: vaporwave2a.flac and vaporwave2b.flac. FLAC is a lossless audio codec, which is usually an indication that retaining fine detail is important to this challenge, which immediately revealed to me that fine and detailed frequency analysis would probably be required. Given that the previous challenge of this series (Vaporwave 1) encoded data in a way visible to a spectrogram, and that this was an audio file, I immediately opened both files for viewing in a spectrogram. Personally, I use Adobe Audition, but Audacity (a popular and free Digital Audio Workstation) would also suffice.

![21.2KHz to 22.9KHz Frequency Range in vaporwave2b.flac](https://raw.githubusercontent.com/swin-scsc/writeups/master/2020/rgbCTF/%5BZTC%5D/images/vaporwave2-zeph-screenshot-1.png)

The first thing that was apparent was a Base64 string in the 21.2KHz to 22.9KHz frequency range in vaporwave2b.flac. This string converts into "well, well, well, how the turntables...". There were no other immediately noticeable major differences between the two files other than that, however, more on this later. 
Already having my suspicions, mainly based on very slight differences in the lower frequency range between vaporwave2a and vaporwave2b, the fact that there were two files, and that the aforementioned “how the turntables” implies flipping or rotating something upside down, I decided to invert the waveform of vaporwave2a.
Inversion of a waveform is simply the act of flipping it upside down. The peaks become troughs, and the troughs become peaks. Here is an example: 

![Inversion Waveform Example](https://totalproaudio.stevebunting.com/wp-content/uploads/2010/08/Figure-3-Dual-Sine-Polarity.png)

The red line represents the original waveform, and the light blue line represents the inverted waveform. The use of this is that two completely equal but opposite waveforms would cancel each other out – if these two audio files had exactly the same data at the exact same frequency, an inversion of one, a mixdown, and then a spectrogram of the newly created file would be completely blank, except for the Base64 hint at the high frequencies - this was not the case.

![Spectrographic view of the difference between vaporwave2a and vaporwave2b](https://raw.githubusercontent.com/swin-scsc/writeups/master/2020/rgbCTF/%5BZTC%5D/images/vaporwave2-zeph-screenshot-2.png)

And that is the point of a waveform inversion – if you perform a waveform inversion to one of two seemingly identical waveforms, all that is left is the difference - and here we are greeted with a flag, in the spectrographic view of the difference between vaporwave2a and vaporwave2b.
### Flag: rgbCTF{s3v3r3_1nv3r71g0}


