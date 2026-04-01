/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* x, ListNode* y) {
        
        ListNode* a = new ListNode(9);
        ListNode*ans = a;
        while(x != NULL && y != NULL){
            if(x->val>=y->val){
                a->next = y;
                y = y->next;
                a = a->next;
                a->next = NULL;
            }
            else{
                a->next = x;
                x = x->next;
                a = a->next;
                a->next = NULL;

            }
        }
        if(x==NULL){
            if(y!= NULL) a->next = y;
            return ans->next;
        }
        if(y==NULL){
            if(x!= NULL) a->next = x;
            return ans->next;
        }
        return ans->next;
        
    }
};
