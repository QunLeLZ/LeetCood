class Solution {
    public String intToRoman(int num) {
        StringBuilder res = new StringBuilder();
        int[] nums = {1000,900,500,400,100,90,50,40,10,9,5,4,1};
        String[] ch = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
        for(int i = 0;i < nums.length;i++){
            int tmp = nums[i];
            if(num >= tmp){
                int x = num /nums[i];
                for(int j = 0;j < x;j++)
                    res.append(ch[i]);
                num = num - tmp * x;
            }
        }
        return res.toString();
    }
}