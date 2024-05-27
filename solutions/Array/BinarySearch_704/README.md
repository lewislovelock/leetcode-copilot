# Intuition

The problem is asking to implement a binary search algorithm. Binary search is a divide-and-conquer algorithm used to find a particular element in a sorted array. The element is always searched in the middle of a portion of the array.

## Approach

Sure. This code implements the binary lookup algorithm, which is a search algorithm that finds a specific element in an ordered array.

First, we define two pointers, `left` and `right`, which point to the beginning and end of the array, respectively. These two pointers define a search interval.

Then, we enter a loop and continue searching as long as `left` is not greater than `right`.

In each loop, we first calculate `middle`, which is the midpoint between `left` and `right`. The calculation `left + (right - left) // 2` is done here to prevent overflow caused by `(left + right) // 2`. When `left` and `right` are both very large, `left + right` may exceed the maximum integer value, causing an overflow. This is not a problem with `left + (right - left) // 2`.

Next, we compare the element at `middle` with the target value `target`. If the element at `middle` is greater than `target`, then `target` should be to the left of `middle`, so we move `right` to `middle - 1`. If the element at `middle` is smaller than `target`, then `target` should be to the right of `middle`, so we move `left` to `middle + 1`. If the element at `middle` is equal to `target`, then we find `target` and return directly to `middle`.

If the loop ends without finding `target`, then we return `-1`, indicating that `target` is not in the array.

## Complexity

- Time complexity: The time complexity is O(log n) because with each comparison, we are reducing the size of the input by half. Here, n is the length of the array.

- Space complexity: The space complexity is O(1) because we are not using any extra space that scales with the input size. We are only using a constant amount of space to store the pointers.

## Code

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else: return mid

        return -1
```
