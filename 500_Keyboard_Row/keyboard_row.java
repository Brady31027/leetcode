public class Solution {
    public String[] findWords(String[] words) {
        
        int[] row1 = convertToArr("qwertyuiop");
        int[] row2 = convertToArr("asdfghjkl");
        int[] row3 = convertToArr("zxcvbnm");
        
        List<String> ans = new LinkedList<>();
        for (String word : words) {
            if ( all(row1, word) || all(row2, word) || all(row3, word) ) {
                ans.add(word);
            }
        }
        return ans.toArray(new String[0]);
    }
    
    private int[] convertToArr(String s) {
        int[] arr = new int[26];
        for (char c : s.toCharArray()) {
            arr[c - 'a'] = 1;
        }
        return arr;
    }
    
    private boolean all(int[] row, String word) {
        for (char c: word.toLowerCase().toCharArray() ) {
            if ( row [ c - 'a'] == 0) return false;
        }
        return true;
    }
}
