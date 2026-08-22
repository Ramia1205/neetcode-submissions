# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        left = dummy
        right = head

        # Move right n nodes ahead
        for i in range(n):
            right = right.next

        # Move BOTH pointers until right reaches the end.
        # Since they're n nodes apart, left will end up
        # directly BEFORE the node we want to remove.
        while right:
            left = left.next
            right = right.next

        # Skip over the node we want to remove
        left.next = left.next.next

        return dummy.next