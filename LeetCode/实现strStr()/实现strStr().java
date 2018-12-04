class Solution {
    public int strStr(String haystack, String needle) {
        int size = needle.length();
        if(needle == "") return 0;
        if(size > haystack.length() || needle == null) return -1;
        for(int i = 0;i <= haystack.length()-size;i++){
            int j = 0;
            for(j = 0;j < size;j++)
                if(haystack.charAt(i+j) != needle.charAt(j))
                    break;
            if(j == size){
                return i;
            }
        }
        return -1;
    }
}