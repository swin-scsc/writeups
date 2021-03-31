# UTCTF - Prove No Knowledge

**Category:** Crypto<br/>
**Points:** 946/1000<br/>
**Solves:** 75<br/>

&nbsp;

> I've been trying to authenticate to this service, but I'm lacking
> enough information.
> nc crypto.utctf.live 4354

&nbsp;

*Write-up By:* [gov](https://github.com/rgovind92)

&nbsp;

## The Challenge
We're given access to a server that implements a [Zero-Knowledge Proof](), providing us the numbers _g_, _y_, and _p_, and asking us to prove our knowledge of a number _x_ that satisifies the following equation.

&nbsp;

<p align="center">
    <img height="24" src="https://render.githubusercontent.com/render/math?math=y = g^x \pmod p">
    <img align="right" height="24" src="https://render.githubusercontent.com/render/math?math=(1)">
</p>

&nbsp;

The challenge has 256 rounds, but only two of them are unique. The first one asks us to send it numbers _r_ and _a_ that satisfy the following equation.

&nbsp;

<p align="center">
    <img height="24" src="https://render.githubusercontent.com/render/math?math=a = g^r \pmod p">
</p>

&nbsp;

The second round asks us to send it the numbers _a_ and _b_ that satisfy the following equations for some number _r_.

&nbsp;

<p align="center">
    <img height="24" src="https://render.githubusercontent.com/render/math?math=a = g^r \pmod p">
</p>
<p align="center">
    <img height="24" src="https://render.githubusercontent.com/render/math?math=b = (x %2B r) \pmod {p - 1}">
    <img align="right" height="24" src="https://render.githubusercontent.com/render/math?math=(2)">
</p>

&nbsp;

## Solution
Round 1 is trivial; We can send _r_ as 0 and send _g<sup>r</sup> mod(p)_ as 1. Round 2 is trickier; It looks like we need to know _x_ in order to pass it. However, as it is with a lot of crypto, things get easier when you write down the equations on paper. Note that if we invert _(1)_, we get the following relation.

&nbsp;

<p align="center">
    <img height="24" src="https://render.githubusercontent.com/render/math?math=y^{-1} = g^{-x} \pmod p">
</p>

&nbsp;

Because we know _y_, we can calculate the left hand side of this equation and send it to the challenge as _g<sup>r</sup> mod(p)_. The value of _r_ for which this is true is, of course, _-x_, making _(2)_ equivalent to the following.

&nbsp;

<p align="center">
    <img height="24" src="https://render.githubusercontent.com/render/math?math=b = (x %2B r) \pmod p = (x - x) \pmod p = 0">
</p>

&nbsp;

Evidently, knowing _x + r (mod p - 1)_ proves no knowledge of _x_. The problem is that the prover knows what challenge the verifier is going to pose them, and so, knowing this, they can choose a convenient _r_. The correct way to do a Zero-Knowledge Proof here is to generate a random number _e_ and ask the prover to send _ex + r (mod p)_ (more details [here](https://crypto.stackexchange.com/questions/70877/is-a-hash-a-zero-knowledge-proof)). Since _e_ is generated _after_ the prover sends _g<sup>r</sup> (mod p)_, there is no way to "spoof" _g<sup>-ex</sup> (mod p)_ (assuming that the RNG used to generate _e_ is cryptographically secure).

As for the flag, authenticate the remaining 254 rounds just like the first two.

&nbsp;

### Flag: utflag{questions_not_random}
