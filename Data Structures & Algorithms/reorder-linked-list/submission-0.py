# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1) Find the middle using slow/fast pointers
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is now around the middle

        # 2) Reverse the second half
        prev = None
        curr = slow.next

        # Split the list into two halves
        slow.next = None

        while curr:
            next_node = curr.next

            curr.next = prev
            prev = curr

            curr = next_node

        # prev is now the head of the reversed second half

        # 3) Merge the two halves
        first = head
        second = prev

        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next