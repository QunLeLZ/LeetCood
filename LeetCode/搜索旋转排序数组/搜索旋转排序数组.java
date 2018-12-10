class Solution {
    public int search(int[] nums, int target) {
        if(nums.length==0){
                return -1;
            }
            int st = 0,end = nums.length-1;
            while(st <= end){
                int mid = st+(end-st)/2;
                if(nums[mid]==target){
                    return mid;
                }
                if(nums[mid]>=nums[st]){
                    if(nums[st]<=target&&target<nums[mid]){
                        end = mid-1;
                    }else{
                        st = mid+1;
                    }
                }else{
                    if(nums[mid]<target&&target<=nums[end]){
                        st = mid+1;
                    }else{

                        end = mid==0?mid:mid-1;
                    }
                }
            }
            return -1;
    }
}