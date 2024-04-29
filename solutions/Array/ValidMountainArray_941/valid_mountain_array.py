from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        """
        >>> Solution().validMountainArray([0,3,2,1])
        True
        >>> Solution().validMountainArray([3,5,5])
        False
        >>> Solution().validMountainArray([0,3,2,1,2])
        False
        """
        left, right = 0, len(arr) - 1

        while left < len(arr) - 1 and arr[left] < arr[left + 1]:
            left += 1

        while right > 0 and arr[right] < arr[right - 1]:
            right -= 1

        return left == right and left != 0 and right != len(arr) - 1