

class Solution {
private:
	vector<vector<int>> res;
public:
    vector<vector<int>> permute(vector<int>& nums) {
    	vector<bool> visited(nums.size(), false);
    	vector<int> cur_res;
    	trace_back(nums, visited, cur_res);
    	return res;
    }

    void trace_back(const vector<int>& nums, vector<bool>& visited, vector<int>& cur_res){
    	if(cur_res.size() == nums.size()){
    		res.push_back(cur_res);  // 装的就是copy过的，所以不用复制哦
    		return;
    	}

    	for(int i = 0; i < nums.size(); i++){
    		if(!visited[i]){
    			visited[i] = true;
    			cur_res.push_back(nums[i]);
    			trace_back(nums, visited, cur_res);
    			visited[i] = false;
    			cur_res.pop_back();
    		}
    	}
    }
};