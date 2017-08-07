public class Solution {
    public int singleNumber(int[] nums) {
        Arrays.sort(nums);
        int prev = nums[0];
        int ref = 1;
        for (int i = 1; i < nums.length; ++i) {
            if (nums[i] != prev) {
                if (ref < 3) {
                    return prev;
                } else {
                    prev = nums[i];
                    ref = 1;
                }
            } else {
                ref += 1;
            }
        }
        return prev;
    }
}
