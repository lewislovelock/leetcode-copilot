# Intuition

The problem is asking to remove all instances of a specific value from an array in-place and return the new length of the array. The order of elements can be changed.

## Approach

We can solve this problem using the two-pointer technique. We maintain two pointers, fast and slow. The fast pointer is used to scan through the array, and the slow pointer keeps track of the position to place the next number that is not equal to val. If the current number pointed by the fast pointer is not equal to val, we copy it to the position pointed by the slow pointer, and then increment the slow pointer. If it is equal to val, we just increment the fast pointer. In this way, all the numbers not equal to val are copied to the front of the array, and the order of these numbers are the same as in the original array.

## Complexity

- Time complexity: The time complexity is O(n) because we are scanning through the array once. Here, n is the length of the array.
- Space complexity: The space complexity is O(1) because we are not using any extra space that scales with the input size. We are only using a constant amount of space to store the pointers.

## Code

```py
from typing import List


class Solution:
    def remove_element(self, nums: List[int], val: int) -> int:
        """
        >>> Solution().remove_element([3,2,2,3], 3)
        2
        >>> Solution().remove_element([0,1,2,2,3,0,4,2], 2)
        5
        """
        fast, slow = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
```
