Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
<pre>
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
</pre>
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
  
***
  
**Note**  
* s = s + " "
  * The reason why we add a space in the tail is because we need to handle the last token
* return ans[:-1]
  * The reason why we remove the last char is because we add an extra space for evary token, but the last token doesn't need a space
