from typing import List


class Solution1:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table = {}
        for num in nums1:
            table[num] = table.get(num, 0) + 1
        
        res = set()
        for num in nums2:
            if num in table:
                res.add(num)
                del table[num]

        return res
    
    
class Solution2:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = [0] * 1001
        count2 = [0] * 1001
        result = []
        for num in nums1:
            count1[num] += 1
        for num in nums2:
            count2[num] += 1
        for i in range(1001):
            if count1[i] * count2[i] > 0:
                result.append(i)
        return result