class Solution {
private:
    unordered_map<char, string> record = {
            {'2', "abc"},
            {'3', "def"},
            {'4', "ghi"},
            {'5', "jkl"},
            {'6', "mno"},
            {'7', "pqrs"},
            {'8', "tuv"},
            {'9', "wxyz"}
        };
        vector<string> res;
public:
    vector<string> letterCombinations(string digits) {
        if(digits.size() == 0)
            return res;

        string cur_res = "";
        helper(digits, 0, cur_res);
        return res;
    }

    void helper(string digits, int start_idx, string& cur_res){
        if(start_idx == digits.size()){
            res.push_back(cur_res);
            return;
        }
        
        for(auto c: record[digits[start_idx]]){
            cur_res += c;
            helper(digits, start_idx + 1, cur_res);
            cur_res.erase(cur_res.size() - 1, 1);
        }
    }
};