class Solution {
    public int divide(int dividend, int divisor) {
        if(divisor == 0 || (dividend == Integer.MIN_VALUE && divisor == -1)){
            return Integer.MAX_VALUE;
        }
        int sign = ((dividend < 0) ^ (divisor < 0)) ? -1 : 1;
        long ms = (long)dividend;
        long ns = (long)divisor;
        ms = Math.abs(ms);
        ns = Math.abs(ns);
        int num = 0;
        while(ms >= ns){
            long m = ns;
            long n = 1;
            while(ms >= (m << 1)){
                m <<= 1;
                n <<= 1;
            }
            num += n;
            ms -= m;
        }
        return num * sign;
    }
}