

class Solution {
private:
    vector<vector<int>> res;
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<bool> visited = vector<bool>(nums.size(), false);
        helper(nums, vector<int>(), visited);
        return res;
    }

    void helper(const vector<int>& nums, vector<int> cur_res, vector<bool> visited){
        if(cur_res.size() == nums.size()){
            res.push_back(cur_res);
            return;
        }
        for(int i = 0; i < nums.size(); i++){
            if(!visited[i]){
                visited[i] = true;
                cur_res.push_back(nums[i]);
                helper(nums, cur_res, visited);
                visited[i] = false;
                cur_res.pop_back();
            }
        }
        return;
    }
};