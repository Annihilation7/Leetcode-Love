/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */


class Solution {
public:
    int maxPathSum(TreeNode* root) {
    	int res = -0x3fffffff;
    	helper(root, res);
    	return res;
    }

    int helper(TreeNode* root, int& res){
    	if(root == nullptr)
    		return 0;
    	int left_value = helper(root->left, res);
    	int right_value = helper(root->right, res);
    	if(left_value < 0)  // 对当前节点产生了负增益
    		left_value = 0;
    	if(right_value < 0)
    		right_value = 0;
    	res = max(res, root->val + left_value + right_value);
    	return max(left_value, right_value) + root->val;
    }
};