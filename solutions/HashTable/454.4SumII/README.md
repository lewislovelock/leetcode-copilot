# Problem

[454. 4Sum II](https://leetcode.com/problems/4sum-ii/submissions/1276185696/)

## Intuition

The problem is to find the number of tuples (i, j, k, l) such that A[i] + B[j] + C[k] + D[l] = 0. A brute force approach would be to check all possible tuples, but this would be too slow. A better approach is to use a hashmap to reduce the time complexity.

## Approach

The approach used here is to divide the four arrays into two groups: nums1 and nums2, nums3 and nums4. For each pair of elements in nums1 and nums2, we calculate their sum and store it in the hashmap, with the sum as the key and the frequency as the value. Then for each pair of elements in nums3 and nums4, we calculate their sum and check if the negative of this sum is in the hashmap. If it is, we add the frequency of this sum in the hashmap to the count. The final count is the total number of tuples that satisfy the condition.

## Complexity

- Time complexity: O(n^2), where n is the length of the input arrays. We need to iterate over all pairs in nums1 and nums2, and all pairs in nums3 and nums4.
- Space complexity: O(n^2), as in the worst case, all possible sums of pairs in nums1 and nums2 will be stored in the hashmap.

## Code

```python
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashmap = {}
        for i in nums1:
            for j in nums2:
                hashmap[i + j] = hashmap.get(i + j, 0) + 1

        count = 0
        for i in nums3:
            for j in nums4:
                count += hashmap.get(- i - j, 0)

        return count
```
