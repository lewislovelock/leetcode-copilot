# Intuition

The problem is asking to return a list where each element is the number of elements in the original list that are strictly smaller than the corresponding element. To solve this, we can use a hash table to store the count of elements smaller than each element.

## Approach

First, we create a new list res, which is a copy of nums. Then we create an empty hash table, hash.

Then we sort res. The index of each element in the sorted res list is the number of elements smaller than it. For example, if res is [1,2,2,3,8], then the number 1 has index 0, which means that there is no number smaller than 1, and the number 2 has index 1, which means that there is a number smaller than 2, namely 1.

Next, we iterate through the sorted res and add each element and its index to the hash table hash. If we encounter the same number, we don't update the hash table because we only care about the index of the first occurrence, and that's because we want the number of numbers that are smaller than the current number, not equal to the current number.

Finally, we traverse the original list of nums again and use the hash table hash to find the index of each element, and then assign that index value to the corresponding position in res. Thus, each element in res becomes a number of elements smaller than the corresponding element in the original nums.

Returning to res gives us the result we want.

## Complexity

- Time complexity: The time complexity is O(n log n) because we are sorting the array. Here, n is the length of the array.

- Space complexity: The space complexity is O(n) because we are using an extra array of the same size as the input array and a hash table to store the counts. The hash table size in the worst case can be equal to the size of the array.

## Code

```py
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = nums[:]
        hash = dict()
        res.sort()
        
        for i, num in enumerate(res):
            if num not in hash.keys():
                hash[num] = i
        for i, num in enumerate(nums):
            res[i] = hash[num]

        return res
```
