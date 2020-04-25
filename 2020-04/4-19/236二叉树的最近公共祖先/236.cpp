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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root == nullptr)
        	return nullptr;

        if(root == p || root == q)
        	return root;

        TreeNode* p_node = lowestCommonAncestor(root->left, p, q);
        TreeNode* q_node = lowestCommonAncestor(root->right, p, q);

        if(p_node == nullptr)
        	return q_node;
        if(q_node == nullptr)
        	return p_node;

        // p_node和q_node都不为空，此时p_node和q_node在root的一左一右，那么root此时就是最近的公共祖先
        // 所以返回root即可。
        return root;
    }
};