from typing import List
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        hashmap = {}
        for i in nums1:
            for j in nums2:
                hashmap[i + j] = hashmap.get(i + j, 0) + 1
        
        for i in nums3:
            for j in nums4:
                count += hashmap.get(- i - j, 0)
                
        return count