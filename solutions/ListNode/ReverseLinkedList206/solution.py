from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        >>> s = Solution()
        >>> node3 = ListNode(3)
        >>> node2 = ListNode(2, node3)
        >>> node1 = ListNode(1, node2)
        >>> reversed_head = s.reverseList(node1)
        >>> reversed_head.val
        3
        >>> reversed_head.next.val
        2
        >>> reversed_head.next.next.val
        1
        """
        cur = head
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

if __name__ == "__main__":
    import doctest
    doctest.testmod()