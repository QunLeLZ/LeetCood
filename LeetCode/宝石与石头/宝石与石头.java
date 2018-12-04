class Solution {
    public int numJewelsInStones(String J, String S) {
        HashMap map = new HashMap();
        int count = 0;
        for(int i = 0;i < J.length();i++){
            map.put(J.charAt(i),0);
        }
        for(int j = 0;j < S.length();j++){
            if(map.containsKey(S.charAt(j))){
                count += 1;
            }
        }
        return count;
    }
}