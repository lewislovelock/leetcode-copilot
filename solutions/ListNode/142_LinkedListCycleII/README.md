# Intuition

[142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/description/)
Given a linked list, we need to find the node where the cycle begins. If there is no cycle, we return null.

## Approach

We can use a set to keep track of the nodes that we have visited. We start from the head of the list and traverse the list. For each node, we check if it is in the visited set. If it is, this node is the start of the cycle and we return it. If it is not, we add it to the visited set and move on to the next node. If we reach the end of the list, it means there is no cycle and we return null.

## Complexity

- Time complexity: O(n), where n is the number of nodes in the linked list. In the worst case, we need to visit all the nodes once.

- Space complexity: O(n), where n is the number of nodes in the linked list. In the worst case, all nodes are added to the set.

## Code

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()

        while head:
            if head in visited:
                return head
            visited.add(head)
            head = head.next

        return None
        
```
