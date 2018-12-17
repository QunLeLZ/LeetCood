class Solution {
    public int lengthOfLastWord(String s) {
        s = s.trim();
        int len = s.length() - 1;
        int count = 0;
        if(s == null || s == " ")
            return 0;
        for(int i = len;i >= 0;--i){
            if(s.charAt(i) == ' ')
                return count;
            count++;
        }
        return count;
    }
}