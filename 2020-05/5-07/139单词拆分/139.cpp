
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        // dp, 状态转移方程： dp[j] = dp[i] && s.substr(i, j - i) in record
        vector<bool> dp(s.size() + 1, false);
        dp[0] = true;
        unordered_set<string> record(wordDict.begin(), wordDict.end());

        for(int i = 0; i < s.size(); ++i)
            for(int j = i + 1; j < dp.size(); ++j)
                if(dp[i] && record.find(s.substr(i, j - i)) != record.end())  // 注意是j-i 而不是j-i+1
                    dp[j] = true;

        return dp[dp.size() - 1];
    }
};