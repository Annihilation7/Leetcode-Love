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
	bool res = false;
public:
    bool isSubtree(TreeNode* s, TreeNode* t) {
    	// 子树的概念：t必须从开始相等节点开始，知道全部的叶子节点都相等才满足条件
    	if(t == nullptr)
    		return true; // 空节点是任意树的子树
    	if(s == nullptr)
    		return false;  // 没找到和t_root值相等的节点

    	// 先要找到对应的根节点的位置
    	res = res || helper(s, t) || isSubtree(s->left, t) || isSubtree(s->right, t);
    	return res;
    }

    bool helper(TreeNode* s, TreeNode* t){
    	if(s == nullptr && t == nullptr)
    		return true;
    	if(t == nullptr || s == nullptr || s->val != t->val)  // 有任何一个为空，均返回false，这里用到了或运算的短路原则
    		return false;
    	return helper(s->left, t->left) && helper(s->right, t->right);
    }
};