class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        int max_day = days[days.size() - 1];
        vector<int> dp(max_day + 1, 0);
        int day_idx = 0;

        for(int i = 1; i < dp.size(); i++){
            if(i != days[day_idx])
                dp[i] = dp[i - 1];
            else{
                dp[i] = min(
                    dp[max(0, i - 1)] + costs[0], 
                    min(dp[max(0, i - 7)] + costs[1], dp[max(0, i - 30)] + costs[2])
                    );
                ++day_idx;
            }
        }
        return dp[dp.size() - 1];
    }
};