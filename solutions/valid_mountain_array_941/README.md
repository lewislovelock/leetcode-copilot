# Intuition

The problem is asking to check if the given array is a mountain array. A mountain array is an array that first strictly increases and then strictly decreases. The array should have at least three elements and the peak should not be at the ends of the array.

## Approach

First, we initialise two pointers, left and right, pointing to the beginning and end of the array, respectively.

Then, we let the left pointer move to the right until it finds a position where the element to its right is no longer greater than it. This position is the apex of the range, or the end of the ascent and the beginning of the descent.

Next, we move the right pointer to the left until we find a position where the element to its left is no longer greater than it. This position is also the vertex of the mountain range.

Finally, we check to see if left and right are pointing to the same location, and if they are, then this is the vertex of the mountain. We also need to check if this vertex is at the beginning or the end of the array, if it is, then this is not a valid array of mountains, because an array of mountains needs to have an ascending and a descending part, so the vertex cannot be at the beginning or the end.

If left and right point to the same position and the position is not at the beginning or end, then True is returned, indicating that this is a valid array of mountains; otherwise False is returned.

## Complexity

- Time complexity: The time complexity is O(n) because in the worst case we traverse the array twice, once from the left and once from the right. Here, n is the length of the array.

- Space complexity: The space complexity is O(1) because we are not using any extra space that scales with the input size. We are only using a constant amount of space to store the two pointers.

## Code

```python
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        left, right = 0, len(arr)-1

        if len(arr) < 3:
            return False

        while left < len(arr)-1 and arr[left] < arr[left+1]:
            left += 1

        while right > 0 and arr[right] < arr[right-1]:
            right -= 1

        return left == right and right != 0 and left != len(arr)-1
```
