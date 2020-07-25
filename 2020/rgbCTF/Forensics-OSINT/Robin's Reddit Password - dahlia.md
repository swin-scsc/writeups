# rgbCTF - Robin's Reddit Password

**Category:** Forensics/OSINT
**Points:** 490/500
**Solves:** 12/30

> I'm Batman!
> 
> Lately Robin's been acting suspicious... I need to see what he's been up to. Can you get me his reddit password? Just don't try to break into reddit's server...
> 
> Tip : Wrap the Password in flag format
> 
> ~M.R#4930, bAse#0001

*Writeup By:* [dahlia](https://github.com/orangeblossomest)

## Solution:

This challenge was significantly easier to complete at my time of completion vs afterwards. At time of my solve the challenge included the hint: `"Cloudflare have been leaking customer HTTPS sessions for months?"`, this hint was later removed.

Searching this term on google brought up a reddit thread with the same title, which I viewed through removeddit:

https://www.removeddit.com/r/programming/comments/5vtv16/cloudflare_have_been_leaking_customer_https/

Next, I searched the page for the term "robin" and located this comment (this comment was not actually deleted so it could have been located simply through reddit):

![Comment Screenshot](https://raw.githubusercontent.com/swin-scsc/writeups/orangeblossomest-uploading-1/2020/rgbCTF/Forensics-OSINT/images/robins_reddit_password-dahlia-screenshot.png)

The relevant section in this comment being `robin       q67PjKP5jcE+7susJjzT7Q==      bird`, with the text `bird` revealing the flag.


### Flag: rbgCTF{bird}
