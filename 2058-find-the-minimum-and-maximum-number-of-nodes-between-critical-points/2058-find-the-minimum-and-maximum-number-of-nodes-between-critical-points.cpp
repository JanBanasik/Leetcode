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

bool checkForCriticalPoint(int a, int b, int c)
{
    return ((a < b && b > c) || (a > b && b < c));
}
class Solution {
public:
    vector<int> nodesBetweenCriticalPoints(ListNode* head)
    {
        int firstCriticalPointPosition = -1;
        int lastSeenCriticalPointPosition = -1;
        int index = 0;
        int minDistance = 10e6;
        while(head -> next && head -> next -> next)
        {
            if(checkForCriticalPoint(head -> val, head -> next -> val, head -> next -> next -> val))
            {
                if(firstCriticalPointPosition == -1) 
                {
                    firstCriticalPointPosition = index + 1;
                }
                else
                {
                    minDistance = min(minDistance, index + 1 - lastSeenCriticalPointPosition);
                }
                lastSeenCriticalPointPosition = index + 1;
            }
            index ++;
            head = head -> next;
        }
        if(firstCriticalPointPosition == lastSeenCriticalPointPosition) return {-1,-1}; 
        return {minDistance, lastSeenCriticalPointPosition - firstCriticalPointPosition};
    }
};