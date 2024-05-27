# Question

[202.Happy Number](https://leetcode.com/problems/happy-number/description/)

## Intuition

The problem is to determine if a number is a "happy number". A happy number is defined as a number which eventually reaches 1 when replaced by the sum of the square of each digit. If it does not reach 1 and enters a cycle, it is not a happy number.

## Approach

The approach used here is to use a set to keep track of all numbers encountered during the process. We repeatedly replace the number by the sum of the squares of its digits, and add each number encountered to the set. If we reach 1, we return True. If we encounter a number we've seen before (which means we've entered a cycle), we return False.

## Complexity

- Time complexity: O(logn), where n is the input number. Each operation makes the number smaller, so the time complexity is logarithmic.
- Space complexity: O(logn), as in the worst case, all logn digits will be stored in the set.

## Code

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
        return n == 1

```
