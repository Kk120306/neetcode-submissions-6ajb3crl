# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Iterate through the linked list 
        # Start connecting the res start to the enxt node
        # Check if the next nodes n
        if not head:
            return False
        
        slowP = head
        fastP = head.next
        while True:
            if fastP == None:
                break

            if slowP is fastP:
                return True
            
            slowP = slowP.next
            fastP = fastP.next
            if fastP == None:
                break
            fastP = fastP.next


        return False

