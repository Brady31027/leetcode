public class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> missingNum = new ArrayList<Integer>();
        Set indices = new HashSet();
        Set values = new HashSet();
        
        for (int i = 0; i < nums.length; i++) {
            indices.add(i+1);
            values.add(nums[i]);
        }
        
        indices.removeAll(values);
        missingNum.addAll(indices);
        return missingNum;
    }
}
