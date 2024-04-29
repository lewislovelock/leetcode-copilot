# Intuition

Given a sorted array, we need to return a sorted array of squares of each number. The challenge here is that squaring a number changes the relative order of numbers. For example, -2 is less than 1, but (-2)^2 is greater than 1^2.

## Approach

We can use a two-pointer approach to solve this problem. We start with one pointer at the beginning of the array and another at the end. We compare the squares of the numbers at these pointers, and we put the larger one at the end of our result array. Then, we move the pointer of the larger number towards the center. We continue this process until we've processed all numbers.

## Complexity

- Time complexity: O(n), where n is the length of the input array. This is because we're processing each number in the array once.
- Space complexity: O(n), where n is the length of the input array. This is because we're creating a new array to store the result.

## Code

```py
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        >>> Solution().sortedSquares([-4,-1,0,3,10])
        [0,1,9,16,100]
        >>> Solution().sortedSquares([-7,-3,2,3,11])
        [4,9,9,49,121]
        """
        i, j, k = 0, len(nums)-1, len(nums)-1
        res = [0] * len(nums)
        while i <= j:
            if nums[i]**2 < nums[j]**2:
                res[k] = nums[j]**2
                j -= 1
            else:
                res[k] = nums[i]**2
                i += 1
            k -= 1
        return res
```
