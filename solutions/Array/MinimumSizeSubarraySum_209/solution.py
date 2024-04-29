from typing import List


class Solution:
    def minSubArrayLen(self, nums: List[int], target: int) -> int:
        """
        >>> s = Solution()
        >>> s.minSubArrayLen([2,3,1,2,4,3], 7)
        2
        >>> s.minSubArrayLen([1,2,3,4,5], 15)
        5
        >>> s.minSubArrayLen([1,2,3,4,5], 11)
        3
        >>> s.minSubArrayLen([1,2,3,4,5], 100)
        0
        """
        n = len(nums)
        if n == 0: return 0

        left, right = 0, 0
        sum = 0
        ans = n + 1
        while right < n:
            sum += nums[right]
            while sum >= target:
                ans = min(ans, right - left + 1)
                sum -= nums[left]
                left += 1
            right += 1

        return 0 if ans == n + 1 else ans