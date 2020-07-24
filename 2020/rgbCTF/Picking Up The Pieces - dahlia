# rgbCTF - Picking Up The Pieces

**Category:** Misc
**Points:** 403/500
**Solves:** 76/93

> Can you help me? I had a flag that I bought at the store, but on the way home, I dropped parts of it on some roads! Now some roads have strings of text, and I can't tell which are part of my flag. I'm very smart and efficient (but somehow not smart or efficient enough to keep my flag), so I know that I took the fastest way from the store back to my house.
>
> I have a map with a list of all 200000 roads between intersections, and what strings are on them. The format of the map is <intersection 1> <intersection 2> <distance> <string on the road>. My house is at intersection 1 and the store is at intersection 200000.
>
> ~qpwoeirut#5057
>
> - map.txt


*Writeup By:* [dahlia](https://github.com/orangeblossomest)

## Solution

In this challenge we were given a text file map.txt containing 200000 lines of text as described in the challenge description in the format <start node> <end node> <cost> <flag value>.

My first thought given this challenge was to use a path finding algorithm, so I used the example given on [Rosetta code](https://rosettacode.org/wiki/Dijkstra%27s_algorithm#Python) to write a simple one in python .

It was not until I was running the script that I considered that the file contained 200000 lines of text aka 200000 possible edges...

Since this meant that my script was probably going to take a very, very long time to finish I decided to have a quick look at the file itself and see if the flag could be discovered manually.

Using the known plaintext "rgbCTF{XXXXX}" I searched the text file and discovered the row: `135893    137329    287162841    bCTF{`

Then, using the given start/end points of the "roads" was able to put together this path

 start|  end |   cost  | string
------|------|---------|-----
129906|135893|650216228|r,rg
135893|137329|287162841|bCTF{
137329|146596|54796009|1m_b
146596|152272|373997764|4d_4
152272|158541|267495804|t_sh0
158541|162867|274589396|pp1ng
157869|162867|4087522|},Co

Combining the strings gives the flag: `rgbCTF{1m_b4d_4t_sh0pp1ng}`. 

This method took me 5 minutes.

I imagine this challenge would have been much more difficult (and required the pathfinding algorithm I had written) if the flag wrapper, and thus known plaintext, hadn't been included!

### Flag: rgbCTF{1m_b4d_4t_sh0pp1ng}





