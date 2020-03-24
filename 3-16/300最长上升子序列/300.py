

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        dp，dp[i]代表以nums[i]结尾时的最长的上升子序列，每到一个索引，都要和前面的nums[j]
        进行大小比较（遍历），来更新dp[i]位置的值。所以状态转移方程为：
        dp[i] = max(dp[i], dp[:i])
        因为以最后一个索引结尾的字符串不一定是最长的上升子序列，所以要返回max(dp)
        *该解法可以优化到O(nlogn)
        """

        if len(nums) == 0:
            return 0

        dp = [1] * len(nums)
        max_length = 1

        for i in range(1, len(dp)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            max_length = max(max_length, dp[i])

        return max_length


"""
O(nlogn)
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        if(nums.size() == 0)
            return 0;

        vector<int> cell;
        cell.push_back(nums[0]);

        vector<int>::const_iterator iter;
        for(iter = nums.begin() + 面试题17.16化妆师; iter != nums.end(); ++iter){
            if((*iter) > cell.back()){
                cell.push_back(*iter);
                continue;
            }
            int l = 0, r = cell.size() - 面试题17.16化妆师;
            while(l < r){
                int mid = l + (r - l) / 2;
                if(cell[mid] < (*iter))
                    l = mid + 面试题17.16化妆师;
                else
                    r = mid;
            }
            cell[l] = *iter;
        }
        return cell.size();
    }
};
"""


if __name__ == '__main__':
    test = Solution()
    print(test.lengthOfLIS([1,3,6,7,9,4,10,5,6]))