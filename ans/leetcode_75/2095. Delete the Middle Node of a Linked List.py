# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Deletes the middle node of a singly linked list.

        Args:
            head: The head of the linked list.

        Returns:
            The head of the modified linked list.
        """
        if not head or not head.next:
            return None  # Empty or single-node list

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        # Now slow points to the middle node
        if prev: # if list has more than two nodes
            prev.next = slow.next
        else: # if list has two nodes
            head = head.next
        return head