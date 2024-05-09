# Intuition

The problem is asking to remove the nth node from the end of the list. A straightforward approach would be to first traverse the list to find its length, then find the node to remove. However, this would require two passes through the list. We can achieve the goal in one pass using a two-pointer technique.

# Approach

We use two pointers, `fast` and `slow`, and initially set them at the dummy head. We first move the `fast` pointer `n+1` steps ahead. Then, we move both `fast` and `slow` pointers one step at a time. By the time `fast` reaches the end of the list, `slow` will be at the `n+1`th node from the end. We then skip the `n`th node from the end by setting `slow.next = slow.next.next`.

# Complexity

- Time complexity: O(L), where L is the length of the list. We are doing a single pass through the list.
- Space complexity: O(1), as we are only using a constant amount of space.

# Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        slow = fast = dummy

        for _ in range(n+1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next =  slow.next.next

        return dummy.next
```