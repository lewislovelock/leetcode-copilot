# Question

[349. Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/submissions/1269228776/)

## Intuition

Given two arrays, the task is to find the intersection of these arrays. The intersection of two arrays is a list of numbers which are present in both the arrays.

## Approach

The approach used here is counting the occurrence of each number in both arrays. We create two count arrays count1 and count2 of size 1001 (assuming the input numbers are in the range 0-1000). We then iterate over nums1 and nums2 and increment the count of each number in the respective count arrays. Finally, we iterate over the range 0-1000 and for each number, if it is present in both count1 and count2 (i.e., count1[i] * count2[i] > 0), we add it to the result array.

## Complexity

Time complexity: O(n + m + 1001), where n and m are the sizes of nums1 and nums2 respectively. We iterate over both arrays and the range 0-1000.
Space complexity: O(1001 + k), where k is the size of the intersection. We use two count arrays of size 1001 and a result array.
