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
        
