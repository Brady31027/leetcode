func numberOf1Bits(n int) int {
    count := 0
    for n > 0 {
        count += 1
        n &= (n-1)
    }
    return count
}
