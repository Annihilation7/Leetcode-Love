
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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* dummyhead = new ListNode(-1);
        ListNode* pre = dummyhead;

        while(l1 != nullptr && l2 != nullptr){
            if(l1->val <= l2->val){
                pre->next = l1;
                l1 = l1->next;
            }
            else{
                pre->next = l2;
                l2 = l2->next;
            }
            pre = pre->next;
        }
        if(l1 != nullptr)
            pre->next = l1;
        else
            pre->next = l2;
        return dummyhead->next;
    }
};