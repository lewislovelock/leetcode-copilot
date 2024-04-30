# Intuition

The problem is asking to remove all the nodes in the linked list that have the value equal to val. We can solve this problem by using a dummy head node and a pointer to traverse the linked list.

## Approach

Initialize a dummy head node and set its next pointer to the head of the linked list.
Initialize a pointer current at the dummy head node.
Traverse the linked list using the current pointer. For each node, check if the value of the next node is equal to val.
If the value of the next node is equal to val, then skip the next node by setting current.next to current.next.next.
If the value of the next node is not equal to val, then move the current pointer to the next node.
After the traversal, the linked list will not contain any node with value equal to val. Return the next of the dummy head node as the head of the updated linked list.
Complexity
Time complexity: O(n), where n is the number of nodes in the linked list. This is because we need to traverse the entire linked list.
Space complexity: O(1), as we are only using a constant amount of space.
Code

## Code

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(next = head)

        current = dummy_head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy_head.next        
```
