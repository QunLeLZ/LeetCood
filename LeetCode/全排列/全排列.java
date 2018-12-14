class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> listList = new ArrayList<>();
        backtracking(listList, nums, 0);
        return listList;
    }
    private static void backtracking(List<List<Integer>> listList, int[] nums, int j) {
 
        if (j == nums.length) {
            List<Integer> list = new ArrayList<>();
            for (int num : nums) list.add(num);
            listList.add(list);
        }
        for (int i = j; i < nums.length; i++) {
            swap(nums, i, j);
            backtracking(listList, nums, j+1);
            swap(nums, i, j);
        }
    }
    private static void swap(int[] nums, int m, int n) {
        int temp = nums[m];
        nums[m] = nums[n];
        nums[n] = temp;
    }
}