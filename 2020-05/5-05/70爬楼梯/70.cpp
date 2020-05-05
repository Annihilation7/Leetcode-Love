

class Solution {
public:
    int climbStairs(int n) {
        // dp[n] = dp[n - 1] + dp[n - 2]
        if(n <= 2)
            return n;

        int i = 1;  // 一层一种爬法
        int j = 2;  // 二层二种爬法
        int res = 0;

        for(int k = 3; k <= n; k++){
            res = i + j;
            i = j;
            j = res;
        }

        return res;
    }
};