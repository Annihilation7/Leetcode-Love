/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
 
class Solution {
public:
    bool isSubtree(TreeNode* s, TreeNode* t) {
        if(!s)
            return false;
        return helper(s, t) || isSubtree(s->left, t) || isSubtree(s->right, t);
    }

    bool helper(TreeNode* s, TreeNode* t){
        if(!s && !t)
            return true;
        if(!s || !t || s->val != t->val)
            return false;
        return helper(s->left, t->left) && helper(s->right, t->right);
    }
};