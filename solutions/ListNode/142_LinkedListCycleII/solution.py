class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        >>> node1 = ListNode(3)
        >>> node2 = ListNode(2)
        >>> node3 = ListNode(0)
        >>> node4 = ListNode(-4)
        >>> node1.next = node2
        >>> node2.next = node3
        >>> node3.next = node4
        >>> node4.next = node2
        >>> s = Solution()
        >>> s.detectCycle(node1) == node2
        True
        """
        visited = set()
        while head:
            if head in visited:
                return head
            visited.add(head)
            head = head.next

        return None

if __name__ == "__main__":
    import doctest
    doctest.testmod()