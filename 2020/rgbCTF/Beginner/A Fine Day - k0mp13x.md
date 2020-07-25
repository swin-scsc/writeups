# rgbCTF - A Fine day

**Category:** Beginner
**Points:** 50
**Solved:** #354
> It's a fine day to break some ciphers!
>
> Sujd jd bgxopksbm ljsu tg tqqjgb xjkubo. Tqqjgb xjkubod tob t qvor vq dhidsjshsjvg xjkubo. Jsd nbp xvgdjdsd vq slv ghribod, t tgm i. Sv bgxopks t cbssbo, rhcsjkcp jsd kctxb jg sub tckutibs (dv t=0, i=1, bsx.) ip t, tgm subg tmm i. Qjgtccp stnb suts rvm 26 tgm xvgwbos js itxn jgsv t xutotxsbo.
>
> Sub tqqjgb xjkubo jdg's obtccp suts dsovgf. Djgxb js'd rvm 26, subob tob vgcp t qbl uhgmobm mjqqbobgs nbpd, lujxu xtg ib btdjcp iohsb qvoxbm. Tgpltp, ubob'd pvho qctf: ofiXSQ{t_qjgb_tqqjgb_xjkubo}

*Writeup by:* k0mp13x

## Process:

This looks like a lot like a mono-alphabetic substitution, but it’s actually an affine substitution. 

This did not really have much impact on the deciphering though.

I used dcode online tools and it detected it automatically.

https://www.dcode.fr/monoalphabetic-substitution



![dcode Monoalphabetic Substitution Solve](https://raw.githubusercontent.com/swin-scsc/writeups/master/2020/rgbCTF/Beginner/images/a_fine_day-k0mp13x-screenshot.png)


### Flag: rgbCTF{a_fine_affine_cipher}
