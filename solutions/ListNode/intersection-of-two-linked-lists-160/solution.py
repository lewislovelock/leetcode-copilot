class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        >>> node1 = ListNode(1)
        >>> node2 = ListNode(2)
        >>> node3 = ListNode(3)
        >>> node4 = ListNode(4)
        >>> node5 = ListNode(5)
        >>> node6 = ListNode(6)
        >>> node7 = ListNode(7)
        >>> node8 = ListNode(8)
        >>> node1.next = node2
        >>> node2.next = node3
        >>> node3.next = node6
        >>> node6.next = node7
        >>> node7.next = node8
        >>> node4.next = node5
        >>> node5.next = node6
        >>> s = Solution()
        >>> intersect = s.getIntersectionNode(node1, node4)
        >>> intersect.val
        6
        """
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)

        if lenA > lenB:
            headA = self.moveForward(headA, lenA - lenB)
        else:
            headB = self.moveForward(headB, lenB - lenA)

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
    
        return None
    
    def getLength(self, head: ListNode) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    
    def moveForward(self, head: ListNode, steps: int) -> ListNode:
        for _ in range(steps):
            head = head.next
        return head

if __name__ == "__main__":
    import doctest
    doctest.testmod()
