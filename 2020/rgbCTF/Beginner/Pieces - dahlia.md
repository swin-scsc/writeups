# rgbCTF - Pieces

**Category:** Beginner 
**Points:**  50/500
**Solves:** 422/436

> My flag has been divided into pieces :( Can you recover it for me?
> 
> ~Quintec#0689
>
> - Main.java
>   - Size: 0.60 KB
>   - MD5: 0ef37e478675de04e468fb1496a5258f


*Writeup By:* [dahlia](https://github.com/orangeblossomest)

## Solution

With this challenge we were provided with one java file, Main.java:

```java
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String input = in.readLine();
        if (divide(input).equals("9|2/9/:|4/7|8|4/2/1/2/9/")) {
            System.out.println("Congratulations! Flag: rgbCTF{" + input + "}");
        } else {
            System.out.println("Incorrect, try again.");
        }
    }
    
    public static String divide(String text) {
        String ans = "";
        for (int i = 0; i < text.length(); i++) {
            ans += (char)(text.charAt(i) / 2);
            ans += text.charAt(i) % 2 == 0 ? "|" : "/";
        }
        return ans;
    }
}
```

Main.java contains two methods, main, and divide.
The main method takes user input as the variable input
```java
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String input = in.readLine(); # takes user input 
```
and then passes input as an argument to the divide method, comparing the output with a string `9|2/9/:|4/7|8|4/2/1/2/9/`, and if the two are equal, prints the user input as the flag:
```java
        if (divide(input).equals("9|2/9/:|4/7|8|4/2/1/2/9/")) {
            System.out.println("Congratulations! Flag: rgbCTF{" + input + "}");
        }
```
So here we can see that if we give in the correct input, the input will be the flag.

To determine flag we need to essentially reverse the divide() method, creating a new method that will take the previous output `9|2/9/:|4/7|8|4/2/1/2/9/` and give the input.

Thankfully divide() is a simple method.

```java
    public static String divide(String text) {
        String ans = "";
        for (int i = 0; i < text.length(); i++) {
            ans += (char)(text.charAt(i) / 2);
            ans += text.charAt(i) % 2 == 0 ? "|" : "/";
        }
        return ans;
    }
```

It takes an input string, and for each character divides its ASCII value by 2, and converts it back to a character, and adds that character to the ans output variable:

```java
 ans += (char)(text.charAt(i) / 2);
```

As we are performing division on ASCII chars, both values are ints, meaning that any result will be truncated towards zero to maintain the result as an integer. To compensate for this divide() has a second line of code

```java
ans += text.charAt(i) % 2 == 0 ? "|" : "/";
```

This checks if the value being divided is divisible by 2, if true, a "|" will be appended to ans, otherwise a "/".

To solve this I wrote a simple python script:

```python
def undivide(text):
    n = 2
    string = [text[i:i+n] for i in range(0, len(text), n)]
    ans = ''
    for i in string:
            x = ord(i[0]) * 2
            if(i[1] == "/"): # if original value was an odd number, += 1 to compensate for int division truncation
                x += 1
            ans += chr(x)
    return ans
    
string = "9|2/9/:|4/7|8|4/2/1/2/9/"

print("Flag: rgbCTF{" + undivide(string) + "}")
```

Running this program in python gives the output:

```bash
kali@kali:~/rgbctf2020/pieces$ python solve.py 
Flag: rgbCTF{restinpieces}
```

### Flag: rgbCTF{restinpieces}





