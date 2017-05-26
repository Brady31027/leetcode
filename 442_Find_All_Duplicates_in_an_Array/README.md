Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
<pre>
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
</pre>
  
***  
  
Note:  

Following snipe of code is doing sorting  
```python
  i = 0
  while i < len(nums):
     if nums[i] != nums[nums[i]-1]:
        nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1] 
     else:
        i += 1
```
