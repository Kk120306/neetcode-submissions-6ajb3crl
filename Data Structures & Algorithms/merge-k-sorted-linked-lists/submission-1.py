# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy

        while True: 
            minVal = -1001
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if minVal == -1001 or lists[minVal].val > lists[i].val:
                    minVal = i
            
            if minVal == -1001:
                break
            cur.next = lists[minVal]
            lists[minVal] = lists[minVal].next
            cur = cur.next

        
        return dummy.next
                