

class Solution {
public:
    int search(vector<int>& nums, int target) {
        // 经典二分查找模板的题
        if(nums.size() == 0)
            return -1;

        int left = 0;
        int right = nums.size() - 1;

        while(left < right){
            int mid = left + (right - left) / 2;
            if(nums[mid] < nums[right]){  // [mid, right]有序
                if(nums[mid] < target && target <= nums[right])
                    left = mid + 1;
                else
                    right = mid;
            }
            else{  // [left, mid]有序
                if(nums[left] <= target && target <= nums[mid])
                    right = mid;
                else
                    left = mid + 1;
            }
        }

        if(nums[left] != target)
            return -1;
        return left;
    }
};