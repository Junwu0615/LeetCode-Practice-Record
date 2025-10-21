"""
"""
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next  # 暫存下一個節點
            curr.next = prev  # 反轉指標
            prev = curr  # 前進 prev
            curr = next_node  # 前進 curr
        return prev  # prev 變成新的頭


# 工具函數：list → linked list
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


# 工具函數：linked list → list（方便印出）
def linked_list_to_list(head):
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4,5]
    head = build_linked_list(nums)
    print(f'head: {head}, ans: {s.reverseList(head)}')

    nums = [1,2]
    head = build_linked_list(nums)
    print(f'head: {head}, ans: {s.reverseList(head)}')

    nums = []
    head = build_linked_list(nums)
    print(f'head: {head}, ans: {s.reverseList(head)}')