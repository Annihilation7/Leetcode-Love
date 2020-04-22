

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */


#include <queue>

 
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
    	if(root == nullptr)
    		return vector<int>();

    	vector<int> res;
    	queue<TreeNode*> q;
    	q.push(root);
    	// empty, size, pop, front, push, back

    	while(!q.empty()){
    		int queue_length = q.size();
    		for(int i = 0; i < queue_length; i++){
	    		TreeNode* pop_elem = q.front();
	    		q.pop();
	    		if(i == 0)
	    			res.push_back(pop_elem->val);
	    		if(pop_elem->right)
	    			q.push(pop_elem->right);
	    		if(pop_elem->left)
	    			q.push(pop_elem->left);
    		}
    	}
    	return res;
    }
};