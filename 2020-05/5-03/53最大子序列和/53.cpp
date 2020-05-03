class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // 经典简单dp
        assert(nums.size() > 0);
        int res = nums[0];

        for(int i = 1; i < nums.size(); i++){
            nums[i] = max(nums[i - 1] + nums[i], nums[i]);
            res = max(res, nums[i]);
        }
        return res;
    }
};