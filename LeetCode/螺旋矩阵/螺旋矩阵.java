class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        if (matrix.length == 0) {
            return new ArrayList<>();
        }
        List<Integer> res = new ArrayList<>();
        int tR=0,tC=0,dR=matrix.length-1,dC=matrix[0].length-1;
        while(tR <= dR && tC <= dC){
            f(res,matrix,tR++,tC++,dR--,dC--);
        }
        return res;
    }
    public static void f(List res,int[][] matrix,int tR,int tC,int dR,int dC){
        if(tR == dR){
            for(int i = tC;i <= dC;i++){
                res.add(matrix[tR][i]);
            }
        }else if(tC == dC){
            for(int i = tR;i <= dR;i++){
                res.add(matrix[i][tC]);
            }
        }else{
            int curC = tC;
            int curR = tR;
            while(curC != dC){
                res.add(matrix[tR][curC]);
                curC++;
            }
            while(curR != dR){
                res.add(matrix[curR][dC]);
                curR++;
            }
            while(curC != tC){
                res.add(matrix[dR][curC]);
                curC--;
            }
            while(curR != tR){
                res.add(matrix[curR][tC]);
                curR--;
            }
        }
    }
}