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
    bool isValidBST(TreeNode* root) {
        if(!root)
            return true;
        
        return isValidBSTRoot(root, nullptr, nullptr);
    }

    bool isValidBSTRoot(TreeNode* root, TreeNode* lower, TreeNode* upper){
        if(!root)
            return true;
        
        if(lower && root->val <= lower->val)
            return false;
        if(upper && root->val >= upper->val)
            return false;

        return isValidBSTRoot(root->left, lower, root) && isValidBSTRoot(root->right, root, upper);
    }
};