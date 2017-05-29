Shuffle a set of numbers without duplicates.

Example:
<pre>
// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
</pre>
  
***
  
**Hint**  
* Algorithm
  * Iteratively traverse from nums[0] to nums[-1] with index i
  * For each i, randomly pick an index from range (i, len(nums)) as anchor
  * Swap nums[i] and nums[anchor]
* Example 
<pre>
nums = [1, 2, 3, 4, 5]
  
i=0, anchor=3
nums = [4, 2, 3, 1, 5]

i=1, anchor=2
nums = [4, 3, 2, 1, 5]
  
i=2, anchor=4
nums = [4, 3, 5, 1, 2]
  
i=3, anchor=3
nums = [4, 3, 5, 1, 2]
  
i=4, anchor=4
nums = [4, 3, 5, 1, 2]
</pre>
