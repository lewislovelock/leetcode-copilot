class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def RemoveNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        >>> node5 = ListNode(5)
        >>> node4 = ListNode(4, node5)
        >>> node3 = ListNode(3, node4)
        >>> node2 = ListNode(2, node3)
        >>> node1 = ListNode(1, node2)
        >>> s = Solution()
        >>> removed = s.RemoveNthFromEnd(node1, 2)
        >>> while removed:
        ...     print(removed.val)
        ...     removed = removed.next
        1
        2
        3
        5
        """
        dummy = ListNode(0, head)
        fast = slow = dummy
        for _ in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return dummy.next


if __name__ == "__main__":
    import doctest

    doctest.testmod()
