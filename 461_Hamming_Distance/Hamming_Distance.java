public class Solution {
    public int hammingDistance(int x, int y) {
        int diff = x ^ y;
        int hamming_dis = 0;
        while (diff > 0) {
            hamming_dis += 1;
            diff &= (diff - 1);
        }
        return hamming_dis;
    }
}
