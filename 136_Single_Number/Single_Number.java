public class Solution {
    public int singleNumber(int[] nums) {
        int total = nums[0];
        for (int i = 1; i < nums.length; ++i) {
            total = total ^ nums[i];
        }
        return total;
    }
}
