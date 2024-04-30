# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        >>> node3 = ListNode(6)
        >>> node2 = ListNode(5, node3)
        >>> node1 = ListNode(4, node2)
        >>> head = ListNode(3, node1)
        >>> s = Solution()
        >>> result = s.removeElements(head, 5)
        >>> result.val
        3
        >>> result.next.val
        4
        >>> result.next.next.val
        6
        """
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next