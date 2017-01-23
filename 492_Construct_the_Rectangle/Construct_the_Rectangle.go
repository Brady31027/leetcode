func constructRectangle(area int) []int {
    ans := []int{area, 1}
    sqrt_num := math.Sqrt((float64(area)))
    sqrt_ceil := int(math.Ceil(sqrt_num))
    for i:= sqrt_ceil; i > 1; i-- {
        if area % i == 0 {
            w := area/i
            if i >= w {
                ans[0] = i
                ans[1] = w
            }else {
                ans[0] = w
                ans[1] = i
            }
            return ans
        }
    }
    return ans // worst case
}
