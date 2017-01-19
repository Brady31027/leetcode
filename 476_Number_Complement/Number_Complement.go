func findComplement(num int) int {
    upper_bound := 1
    for upper_bound <= num {
        upper_bound <<= 1
    }
    return (upper_bound - 1 ) ^ num
}
