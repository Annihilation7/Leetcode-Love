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
private:
	int res = 0;
public:
    int diameterOfBinaryTree(TreeNode* root) {
    	// 本题可以转化成某个根节点的左子树的高度+右子树的高度
    	helper(root);
    	return res;
    }

    int helper(TreeNode* root){
    	if(root == nullptr)
    		return 0;
    	int left_height = helper(root->left);
    	int right_height = helper(root->right);
    	// 回溯的时候求每层树的树高，就两层递归，刚才那个4层递归。。。
    	res = max(res, left_height + right_height);
    	return 1 + max(left_height, right_height);  // 当前节点为根的二叉树的树高
    }
};