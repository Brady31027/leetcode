func twoSum(nums []int, target int) []int {
    result_map := map[int] int {}
    i := 0
    for i < len(nums) {
        if val, existed := result_map[target-nums[i]]; existed {
            return []int{val, i}
        }
        result_map[nums[i]] = i
        i++
    }
    return []int{0,0} // we should never come here!
}
