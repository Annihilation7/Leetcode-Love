/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if(lists.size() == 0)
            return nullptr;

        int k = lists.size();

        while(k > 1){
            int idx = 0;  // 代表了合并后下次的有效容量
            for(int i = 0; i < k; i += 2){
                if(i == k - 1)  // 奇数的情况
                    lists[idx++] = lists[i];
                else
                    lists[idx++] = mergetTwoList(lists[i], lists[i + 1]);
            }
            k = idx;
        }
        return lists[0];  // 最后剩的这个链表就是两两合并后的最终的链表
    }

    ListNode* mergetTwoList(ListNode* l1, ListNode* l2){
        ListNode* dummyhead = new ListNode(-1);
        ListNode* pre_node = dummyhead;

        while(l1 != nullptr && l2 != nullptr){
            if(l1->val <= l2->val){
                pre_node->next = l1;
                l1 = l1->next;
            }
            else{
                pre_node->next = l2;
                l2 = l2->next;
            }
            pre_node = pre_node->next;
        }
        if(l1 != nullptr)
            pre_node->next = l1;
        else
            pre_node->next = l2;

        return dummyhead->next;
    }
};