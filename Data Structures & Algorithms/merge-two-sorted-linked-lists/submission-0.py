# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        # current points to the last node we've added
        current = dummy

        # Keep going while BOTH lists still have nodes
        while list1 and list2:

            # Whichever value is smaller gets added next
            if list1.val < list2.val:
                current.next = list1

                # Move list1 to its next node
                list1 = list1.next

            else:
                current.next = list2

                # Move list2 to its next node
                list2 = list2.next

            # Move current forward to the node we just added
            current = current.next

        # At this point, one list is empty.
        # Attach whatever remains of the other list.
        if list1:
            current.next = list1
        else:
            current.next = list2

        # dummy was just our fake starting node,
        # so the actual answer begins at dummy.next
        return dummy.next