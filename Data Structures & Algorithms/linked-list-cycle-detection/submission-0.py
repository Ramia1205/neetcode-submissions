# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        # fast moves 2 nodes at a time, so we need
        # to make sure both fast and fast.next exist
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next

            # If there's a cycle, fast will eventually
            # catch up to slow
            if slow == fast:
                return True

        # If fast reaches the end, there is no cycle
        return False