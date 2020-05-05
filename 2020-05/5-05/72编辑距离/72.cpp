

class Solution {
public:
    int minDistance(string word1, string word2) {
        vector<vector<int>> dp(word1.size() + 1, vector<int>(word2.size() + 1, 0));

        // 边界1
        for(int i = 1; i < word1.size() + 1; i++)
            dp[i][0] = dp[i - 1][0] + 1;

        // 边界2
        for(int i = 1; i < word2.size() + 1; i++)
            dp[0][i] = dp[0][i - 1] + 1;

        // dp
        for(int i = 1; i < word1.size() + 1; i++)
            for(int j = 1; j < word2.size() + 1; j++){
                if(word1[i - 1] == word2[j - 1])  // 注意是i - 1 和 j - 1!!! 因为dp左上角代表的是空字符串
                    dp[i][j] = dp[i - 1][j - 1];
                else
                    dp[i][j] = min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1])) + 1;
            }

        return dp[word1.size()][word2.size()];
    }
};