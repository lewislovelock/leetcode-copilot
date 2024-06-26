class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self) -> None:
        """
        >>> linked_list = MyLinkedList()
        >>> linked_list.size
        0
        """
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        """
        >>> linked_list = MyLinkedList()
        >>> linked_list.addAtHead(1)
        >>> linked_list.get(0)
        1
        """
        if index < 0 or index >= self.size:
            return -1
        cur = self.dummy_head.next
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        >>> linked_list = MyLinkedList()
        >>> linked_list.addAtHead(1)
        >>> linked_list.get(0)
        1
        """
        self.dummy_head.next = ListNode(val, self.dummy_head.next)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        >>> linked_list = MyLinkedList()
        >>> linked_list.addAtTail(1)
        >>> linked_list.get(0)
        1
        """
        cur = self.dummy_head
        while cur.next:
            cur = cur.next
        cur.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        >>> linked_list = MyLinkedList()
        >>> linked_list.addAtIndex(0, 1)
        >>> linked_list.get(0)
        1
        """
        if index < 0 or index > self.size:
            return

        cur = self.dummy_head
        for _ in range(index):
            cur = cur.next
        cur.next = ListNode(val, cur.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        >>> linked_list = MyLinkedList()
        >>> linked_list.addAtHead(1)
        >>> linked_list.deleteAtIndex(0)
        >>> linked_list.get(0)
        -1
        """
        if index < 0 or index >= self.size:
            return

        cur = self.dummy_head
        for _ in range(index):
            cur = cur.next
        cur.next = cur.next.next
        self.size -= 1
