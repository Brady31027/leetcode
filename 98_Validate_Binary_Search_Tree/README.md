Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
<pre>
    2
   / \
  1   3
</pre>
Binary tree [2,1,3], return true.
Example 2:
<pre>
    1
   / \
  2   3
</pre>
Binary tree [1,2,3], return false.  
  
**Algorithm**
* Use a stack to maintain the traversed nodes
* If root has left child, go left to the leaf
  * This is where we can reach the minimal value in a BST
* If current root is a leaf and there is no left child, we start to pop from stack
  * The popped node is the parent of the current root, so the popped node  should be greater than current root which is a leaf
  * Update root to the right child of the popped node  
* The whold algorithm needs to traverse all nodes in a BST, thus the complexity is O(n)  
   
**Follow-up**
* How to solve it applying recursive approach ?
