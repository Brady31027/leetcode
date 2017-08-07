public class Solution {
    public boolean judgeSquareSum(int c) {
        int head = 0;
        int tail = (int)Math.sqrt(c);
        while (head <= tail) {
            int sum = head * head + tail * tail;
            if (sum == c) return true;
            else if (sum < c) head += 1;
            else tail -= 1;
        }
        return false;
    }
}
