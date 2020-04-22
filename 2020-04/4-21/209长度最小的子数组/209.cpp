//
// Created by 马振宇 on 2020-04-22.
// 因为全是正数，所以是一道滑动窗口的题。滑动窗口的题，注意循环不变量的使用方式
//


class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        int l = 0;
        int r = -1;  // 初始化的时候滑动窗口为空，因为是左闭右闭区间
        int sum = 0;
        int res = nums.size() + 1;

        while(l < nums.size()){ //l和r都可以等于nums.size()-1，也是有效区间
            if(r + 1 < nums.size() && sum < s)
                sum += nums[++r];
            else
                sum -= nums[l++];

            if(sum >= s)
                res = min(res, r - l + 1);
        }

        if(res == nums.size() + 1)
            return 0;
        return res;
    }
};