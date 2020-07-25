# rgbCTF - Penguins

**Category:** Misc 
**Points:** 295/500
**Solves:** 127/135

> \*waddle waddle\*
> 
> ~BobbaTea#6235, Klanec#3100
> 
> - 2020-06-29-173949.zip
>   - Size: 36.83 KB
>   - MD5: 1004f8958054fd7862b75e151c756c26


*Writeup By:* [dahlia](https://github.com/orangeblossomest)

## Solution

We were given one file `2020-06-29-173949.zip`, which was a compressed git repository.  Initial examination of the files included didn't reveal anything, so I assumed that the flag was hidden in a previous commit.

I first located the head file of the repo:

```git
0000000000000000000000000000000000000000 9dcf170a0fb6ae21b5299669b4336a6324c0c316 John Doe <John@doe.com> 1593464930 +0000    commit (initial): first commit
9dcf170a0fb6ae21b5299669b4336a6324c0c316 1117a337faf1ac693cf26bb3bcccb3caa0381d6d John Doe <John@doe.com> 1593464967 +0000    commit: birds are cool
1117a337faf1ac693cf26bb3bcccb3caa0381d6d 1117a337faf1ac693cf26bb3bcccb3caa0381d6d John Doe <John@doe.com> 1593464995 +0000    checkout: moving from master to feature1
1117a337faf1ac693cf26bb3bcccb3caa0381d6d 955eeb70bcb49d8de331b61f38219bccb7e8f933 John Doe <John@doe.com> 1593465063 +0000    commit: add content
955eeb70bcb49d8de331b61f38219bccb7e8f933 7d6997a74cfa2b5e266355d33fd73c76c9fe9b75 John Doe <John@doe.com> 1593465146 +0000    commit: cooler bird
7d6997a74cfa2b5e266355d33fd73c76c9fe9b75 1117a337faf1ac693cf26bb3bcccb3caa0381d6d John Doe <John@doe.com> 1593465153 +0000    checkout: moving from feature1 to master
1117a337faf1ac693cf26bb3bcccb3caa0381d6d 8ee62379b45217202e75011966b813512cafcbb0 John Doe <John@doe.com> 1593465185 +0000    commit: added an interesting file
8ee62379b45217202e75011966b813512cafcbb0 b474ae165218fec38ac9fb8d64f452c1270e68ea John Doe <John@doe.com> 1593465223 +0000    commit: some new info
b474ae165218fec38ac9fb8d64f452c1270e68ea 102b03d19f932fc5e76d460604804dd522d6850d John Doe <John@doe.com> 1593465324 +0000    commit: some more changes
102b03d19f932fc5e76d460604804dd522d6850d 27440c52e8a7a3d2e50f8fcdee0a88b0f937598d John Doe <John@doe.com> 1593465369 +0000    commit (merge): Merge branch 'feature1'
27440c52e8a7a3d2e50f8fcdee0a88b0f937598d b474ae165218fec38ac9fb8d64f452c1270e68ea John Doe <John@doe.com> 1593465694 +0000    checkout: moving from master to b474ae1
b474ae165218fec38ac9fb8d64f452c1270e68ea b474ae165218fec38ac9fb8d64f452c1270e68ea John Doe <John@doe.com> 1593465718 +0000    checkout: moving from b474ae165218fec38ac9fb8d64f452c1270e68ea to fascinating
b474ae165218fec38ac9fb8d64f452c1270e68ea d14fcbfd3c916a512ad1b956cd19fb7be16c20c6 John Doe <John@doe.com> 1593465745 +0000    commit: an irrelevant file
d14fcbfd3c916a512ad1b956cd19fb7be16c20c6 cfd97cd36fe6c5e450d5057bf25aa1d7ddeca9ef John Doe <John@doe.com> 1593465781 +0000    commit: add content to irrelevant file
cfd97cd36fe6c5e450d5057bf25aa1d7ddeca9ef 5dcac0eddbcb4bffdec552a1172f84762a0b4174 John Doe <John@doe.com> 1593465822 +0000    commit: another perhaps relevant file
5dcac0eddbcb4bffdec552a1172f84762a0b4174 fb70ca39a7437eaba2850703018e1cf9073789e6 John Doe <John@doe.com> 1593465988 +0000    commit: probably not relevant
fb70ca39a7437eaba2850703018e1cf9073789e6 57adae71c223a465b6db3a710aab825883286214 John Doe <John@doe.com> 1593466025 +0000    commit: relevant file
[ommitted]
57adae71c223a465b6db3a710aab825883286214 800bcb90123137a6ee981c93c140bd04c75f507f John Doe <John@doe.com> 1593466646 +0000    commit: some things are not needed
800bcb90123137a6ee981c93c140bd04c75f507f 27440c52e8a7a3d2e50f8fcdee0a88b0f937598d John Doe <John@doe.com> 1593466672 +0000    checkout: moving from fascinating to master
```

Using this, I used git show to check the commit details for every commit, where I discovered this commit containing what appeared to be base64.

```bash
kali@kali:~/rgbctf2020/penguins/git$ git show fb70ca39a7437eaba2850703018e1cf9073789e6
commit fb70ca39a7437eaba2850703018e1cf9073789e6
Author: John Doe <John@doe.com>
Date:   Mon Jun 29 21:26:28 2020 +0000

    probably not relevant

diff --git a/perhaps_relevant_v2 b/perhaps_relevant_v2
new file mode 100644
index 0000000..ad12bc5
--- /dev/null
+++ b/perhaps_relevant_v2
@@ -0,0 +1 @@
+YXMgeW9kYSBvbmNlIHRvbGQgbWUgInJld2FyZCB5b3UgaSBtdXN0IgphbmQgdGhlbiBoZSBnYXZlIG1lIHRoaXMgLS0tLQpyZ2JjdGZ7ZDRuZ2wxbmdfYzBtbTE3c180cjNfdU5mMHI3dW40NzN9
[01:13]
```

Base64 decoding this string `YXMgeW9kYSBvbmNlIHRvbGQgbWUgInJld2FyZCB5b3UgaSBtdXN0IgphbmQgdGhlbiBoZSBnYXZlIG1lIHRoaXMgLS0tLQpyZ2JjdGZ7ZDRuZ2wxbmdfYzBtbTE3c180cjNfdU5mMHI3dW40NzN9` (using [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)&input=WVhNZ2VXOWtZU0J2Ym1ObElIUnZiR1FnYldVZ0luSmxkMkZ5WkNCNWIzVWdhU0J0ZFhOMElncGhibVFnZEdobGJpQm9aU0JuWVhabElHMWxJSFJvYVhNZ0xTMHRMUXB5WjJKamRHWjdaRFJ1WjJ3eGJtZGZZekJ0YlRFM2MxODBjak5mZFU1bU1ISTNkVzQwTnpOOQ)), gave this text, including the flag:
```
as yoda once told me "reward you i must"
and then he gave me this ----
rgbctf{d4ngl1ng_c0mm17s_4r3_uNf0r7un473}
```

### Flag: rgbctf{d4ngl1ng_c0mm17s_4r3_uNf0r7un473}





