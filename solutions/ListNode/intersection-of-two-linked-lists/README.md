# Problem

[160.Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)

# Intuition

The problem is asking to find the intersection node of two linked lists. If there is no intersection, return null. The intersection of two linked lists begins at the node where the two lists merge.

# Approach

The approach used here is to first calculate the lengths of both linked lists. Then, move the head of the longer list forward by the difference in lengths. Now, both lists are of equal length from the potential intersection point to the end. Then, traverse both lists simultaneously until an intersection point is found (where headA == headB) or the end of the lists is reached.

# Complexity

- Time complexity: O(m + n), where m and n are the lengths of the two linked lists. This is because we are traversing both linked lists.
- Space complexity: O(1), as we are not using any additional space that scales with the input size.

# Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
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
```