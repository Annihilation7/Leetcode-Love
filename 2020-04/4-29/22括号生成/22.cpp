

class Solution {
private:
    vector<string> res;
public:
    vector<string> generateParenthesis(int n) {
        string cur_res = "";
        helper(n, n, cur_res);
        return res;
    }

    void helper(int left_residual, int right_residual, string cur_res){
        if(left_residual == 0 && right_residual == 0){
            res.push_back(cur_res);
            return;
        }

        // 剪枝，因为已经不可能是有效括号了。
        if(left_residual > right_residual)
            return;

        if(left_residual > 0)
            helper(left_residual - 1, right_residual, cur_res + '(');
        if(right_residual > 0)
            helper(left_residual, right_residual - 1, cur_res + ')');
    }
};