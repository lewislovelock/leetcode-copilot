# **直觉**

这个问题要求反转一个单链表。解决的思路是遍历链表，对于每个节点，将其下一个节点指向其前一个节点。

## **方法**

1. 初始化三个指针：`cur` 指向 `head`，`pre` 指向 `None`，和 `next`。
2. 遍历链表，直到 `cur` 不是 `None`。
3. 在每次迭代中，首先保存 `cur.next` 到 `next`。
4. 然后更新 `cur.next` 为 `pre` 来反转链接。
5. 最后，将 `pre` 和 `cur` 向前移动一步。
6. 在循环结束时，`pre` 将指向反转列表的新头节点。

## **复杂度**

- 时间复杂度：O(n)，其中 n 是列表中的节点数。我们对每个节点做常数级别的工作。
- 空间复杂度：O(1)，因为我们只使用了常数级别的空间。

## 代码

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        pre = None
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre
```
