func singleNumber(nums []int) int {
    arr_size:=len(nums)
    sort.Ints(nums)
    for k, v := range nums {
        if k > 0 && k % 2 != 0 {
            if v != nums[k-1] {
                return nums[k-1]
            }
        }  
    }
    return nums[arr_size-1]
}
