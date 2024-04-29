from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """
        >>> Solution().smallerNumbersThanCurrent([8,1,2,2,3])
        [4, 0, 1, 1, 3]
        >>> Solution().smallerNumbersThanCurrent([6,5,4,8])
        [2, 1, 0, 3]
        >>> Solution().smallerNumbersThanCurrent([7,7,7,7])
        [0, 0, 0, 0]
        """
        res = nums[:]
        hash = dict()
        res.sort()
        
        for i, num in enumerate(res):
            if num not in hash.keys():
                hash[num] = i
        for i, num in enumerate(nums):
            res[i] = hash[num]

        return res

if __name__ == "__main__":
    import doctest
    doctest.testmod()