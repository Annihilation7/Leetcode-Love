

class Solution {
public:
    int jump(vector<int>& nums) {
        int start = 0, end = 0; // 左闭右闭区间
        int time = 0;

        while(end < nums.size() - 1){
            int max_pos = 0;
            for(int i = start; i <= end; i++){
                max_pos = max(max_pos, i + nums[i]);
                if(max_pos == nums.size()- 1)  // 提前终止一下
                    return time + 1;
            }
            start = end + 1;
            end = max_pos;
            time++;
        }
        return time;
    }
};