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