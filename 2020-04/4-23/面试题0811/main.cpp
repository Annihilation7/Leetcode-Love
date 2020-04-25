//
// Created by nofalling on 2020/4/23.
// 完全背包问题，注意coin以及钱币的遍历顺序


class Solution {
public:
    int waysToChange(int n) {
    	int coins[4] = {25, 10, 5, 1};
    	int* dp = new int[n + 1]();  // 调用()就有默认初始化函数了，初始化为0
    	dp[0] = 1;

    	for(int coin_idx = 0; coin_idx < 4; coin_idx++){
    		for(int i = coins[coin_idx]; i <= n; i++){
    			dp[i] = (dp[i] + dp[i - coins[coin_idx]]) % 1000000007;
    		}
    	}

    	return dp[n];
    }
};