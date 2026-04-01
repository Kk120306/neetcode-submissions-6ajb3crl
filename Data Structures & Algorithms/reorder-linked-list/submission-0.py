# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Iterate through the list and find the middle node 
        left, right = head, head.next
        while right and right.next:
            left = left.next
            right = right.next.next
        
        # Reversing the linked list 
        second = left.next
        prev = left.next = None
        while second: 
            tmp = second.next
            second.next = prev
            prev = second 
            second = tmp

        # Merge them together
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


        
