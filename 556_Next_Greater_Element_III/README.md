Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:
<pre>
Input: 12
Output: 21
</pre>
Example 2:
<pre>
Input: 21
Output: -1
</pre>
  
***
  
Same as Next Permutation  
* Find anchor
* Swap anchor and the one which is greater than anchor from tail
* Sort the tailing range
 
