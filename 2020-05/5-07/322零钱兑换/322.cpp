

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        // 状态转移方程：dp[i] = min(dp[i], dp[i - coin] + 1)
        vector<int> dp(amount + 1, INT_MAX);
        dp[0] = 0;

        for(int i = 1; i < dp.size(); ++i)
            for(const int& coin: coins)
                if(i - coin >= 0 && dp[i - coin] != INT_MAX)
                    dp[i] = min(dp[i], dp[i - coin] + 1);

        return dp[amount] == INT_MAX ? -1 : dp[amount];
    }
};