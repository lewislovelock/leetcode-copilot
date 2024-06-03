# Problem

[383 LeetCode](https://leetcode.com/problems/ransom-note/description/)

## Intuition

The problem is to determine if the `ransomNote` can be constructed from the `magazine`. This can be solved by counting the frequency of each character in the `magazine` and then checking if we have enough of each character in the `magazine` to construct the `ransomNote`.

## Approach

The approach used here is to first count the frequency of each character in the `magazine` using a dictionary. Then, for each character in the `ransomNote`, we check if it exists in the dictionary and if its count is greater than 0. If it doesn't exist or its count is 0, we return `False` as the `ransomNote` cannot be constructed. If it does exist and its count is greater than 0, we decrement the count in the dictionary. If we can successfully iterate through all characters in the `ransomNote`, we return `True`.

## Complexity

- Time complexity: O(n + m), where n is the length of `ransomNote` and m is the length of `magazine`. This is because we iterate through each character in both `ransomNote` and `magazine`.
- Space complexity: O(m), where m is the length of `magazine`. This is the space required to store the character counts in the dictionary.

## Code

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = {}
        for c in magazine:
            counts[c] = counts.get(c, 0) + 1
        for c in ransomNote:
            if c not in counts or counts[c] == 0:
                return False
            counts[c] -= 1
        return True

```