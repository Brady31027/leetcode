Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
<pre>
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
</pre>
The two words can be "abcw", "xtfn".

Example 2:
<pre>
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
</pre>
The two words can be "ab", "cd".

Example 3:
<pre>
Given ["a", "aa", "aaa", "aaaa"]
Return 0
</pre>
