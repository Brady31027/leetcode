func reverseString(s string) string {
    reverse_string := []rune(s)
    for head, tail := 0, len(s) - 1; head < tail ; head, tail = head + 1, tail - 1 {
        reverse_string[head], reverse_string[tail] = reverse_string[tail], reverse_string[head]
    }
    return string(reverse_string)
}
