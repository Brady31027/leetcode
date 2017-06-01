Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
<pre>
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
</pre>
  
***
**Note**  
* Investigate the whole area from the boarders
* newX will be the left neighbor and the right neighbor
  * Take care of the boundary issue and repeat issue
  * To solve the boundary issue, make sure 0 < newX < len(arr) - 1
  * To solve the repeat issue, use a visited map to memorize the investigated area
* If outside height is higher than the inside height, we can trap rain
  * Trapped amount is (outside_height - inside_height)
  * Propagate the outside height to the inside height
  * Push (modified_height, newX) to heap
* If outside height is lower than the inside height, we can not trap rain
  * Push (original_height, newX) to heap 
  
*** 
#heap  
#greedy

