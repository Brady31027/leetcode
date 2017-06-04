Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:
<pre>
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
</pre>
  
***  
**Analysis
* If we read digits [0-9]
  * n = n * 10 + int(c)
* If we read '['
  * Digits are finished  
    ```python
      numStack.append(n)
      n = 0  
    ```
  * Save current value in mainStack to bakStack and ready for the next char  
    ```python
     bakStack.append(mainStack)
     mainStack = []
    ```  
* If we read char
  * mainStack.append(c)
* If we read ']' 
  * A sequence is over, composite the substring sequence  
  ```python
   bakStack[-1].extend(mainStack * numStack.pop())
  ```  
  * After composition, restore to mainStack  
  ```python
   mainStack = bakStack.pop()  
  ```  
