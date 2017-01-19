func hammingDistance(x int, y int) int {
    var dis int = x ^ y
    var count int = 0
    for dis > 0 {
        count += 1
        dis &= (dis-1)
    }
    return count
}
