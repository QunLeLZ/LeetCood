class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> tmp = new ArrayList<>();
        Arrays.sort(candidates);
        if(candidates[0] > target || candidates.length == 0)
            return res;
        f(candidates,res,tmp,0,target);
        return res;
    }
    
    public void f(int[] candidates,List<List<Integer>> res,List<Integer> tmp,int start,int remain){
        if(remain < 0){
            return;
        }else if(remain == 0){
            res.add(new ArrayList<>(tmp));
            return;
        }else{
            for(int i = start;i < candidates.length;i++){
                tmp.add(candidates[i]);
                f(candidates,res,tmp,i,remain-candidates[i]);
                tmp.remove(tmp.size()-1);
            }
        }
    }
}