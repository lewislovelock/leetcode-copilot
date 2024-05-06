# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

## Approach
<!-- Describe your approach to solving the problem. -->
1. Initialize three pointers: `cur` pointing to `head`, `pre` pointing to `None`, and `next`.
2. Traverse the list until `cur` is not `None`.
3. In each iteration, first save `cur.next` in `next`.
4. Then update `cur.next` to `pre` to reverse the link.
5. Finally, move `pre` and `cur` one step forward.
6. At the end of the loop, `pre` will be pointing to the new head node of the reversed list.

## Complexity

- Time complexity: O(n), where n is the number of nodes in the list. We are doing constant work for each node.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: O(1), as we are only using a constant amount of space.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

## Code

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
