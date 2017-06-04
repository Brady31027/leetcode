One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.
<pre>
     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
</pre>
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

Example 1:
<pre>
"9,3,4,#,#,1,#,#,2,#,6,#,#"
Return true
</pre>
Example 2:
<pre>
"1,#"
Return false
</pre>
Example 3:
<pre>
"9,#,#,1"
Return false
</pre>
  
***
**Note**  
* https://discuss.leetcode.com/topic/35976/7-lines-easy-java-solution?page=1 
  * Use indegree and outdegree to determine whether it is valid
  * Hold for pre-order and post-order, seems not fit for in-order
