Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
<pre>
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
</pre>

***
 
**Algo**  
* Step1: Scan from tail to head, check whether nums[x] > nums[x-1], mark x-1 as anchor
* Step2: Scan from tail to head, check if nums[y] > nums[anchor], swap them
  * <pre> 
      E.g. Given nums = [2, 4, 3, 1], nums[0] < nums[1], so anchor = 0  
           Swap nums[anchor] and nums[y] which is nums[2] = 3.
           New nums = [3, 4, 2, 1]
    </pre>  
  * Underlying theory is that, for an descending sub-sequence such as [x] + [4, 3, 1], [4, 3, 1] is the last combination of all its permutations. The only thing we can do is to swap y in [4, 3, 1] and [x] if y > x. 
* Step3: Sort or reverse nums[anchor+1:] to adjust the swapped list. Using the above case as an example.
  * <pre>
      After swap, we have [3, 4, 2, 1] and anchor = 0, simply revert() or sort() the nums[anchor + 1:].
      We will get new list [3, 1, 2, 4] which is the answer 
    </pre>
  * The reason why we do this adjustment is because we've changed the leading digit, the remaining digits need to be sorted in descending order to represent the starting combination subject to the changed leading digit.   
  
***  

Test Case 1:
Given nums = [1, 2, 3]  
* nums[1] = 2 < nums[2] = 3, anchor = 1
* Swap nums[anchor] and nums[y] = nums[2] because nums[anchor] < nums[2] to form [1, 3, 2]
* Sort nums[anchor+1:] which is nums[2:]. The result stays the same as [1, 3, 2]
  
Test Case 2:
Given [3, 2, 1]  
* anchor is -1 because all digits are in decending order
* This is a special case because the sequence is the last combination of all its permutations. In this case, we don't have to swap anything. 
* All we can do is to rollback to its staring combination which is [1, 2, 3]. Therefore applying sorted(nums[anchor+1:] which is sorted(nums[0:]) is good for out purpose.
  
Test Case 3:
Given [4, 2, 0, 2, 3, 1]  
* anchor = 3, and nums[3] = 2
* Swap nums[anchor] and nums[4] to form [4, 2, 0, 3, 2, 1]
* Adjust nums[anchor + 1: ] to form [4, 2, 0, 3, 1, 2] which is the answer  
  
Test Case 4:
Given [1, 2]
* anchor = 0 because nums[0] < nums[1]
* Swap nums[anchor] = nums[0] and nums[y] = nums[1] to form [2, 1]
* Adjust nums[anchor+1:] which is nums[1:]. Result stays the same, ans it's the answer  
 


