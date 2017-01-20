func findMaxConsecutiveOnes(nums []int) int {
    var max, cnt int = 0, 0
    for _, d := range nums {
        if d == 1 {
            cnt += 1
        }else {
            cnt = 0
        }
        if cnt > max {
            max = cnt
        }
    }
    return max
}
