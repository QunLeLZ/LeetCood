class Solution {
    public String addBinary(String a, String b) {
        String result = "";
        boolean carry = false;
        int counter = Math.max(a.length(), b.length());
        for (int i = 1; i <= counter; i++) {
            int idxA = a.length() - i;
            int idxB = b.length() - i;
            char c1 = idxA >= 0 ? a.charAt(idxA) : '0';
            char c2 = idxB >= 0 ? b.charAt(idxB) : '0';

            if (!carry) {
                if (c1 == '1' && c2 == '1') {
                    carry = true;
                    result = "0" + result;
                } else if (c1 == '1' || c2 == '1') {
                    result = "1" + result;
                } else {
                    result = "0" + result;
                }
            } else {
                if (c1 == '1' && c2 == '1') {
                    result = "1" + result;
                } else if (c1 == '1' || c2 == '1') {
                    result = "0" + result;
                } else {
                    carry = false;
                    result = "1" + result;
                }
            }
        }

        if (carry) {
            result = "1" + result;
        }
        return result;
    }
}