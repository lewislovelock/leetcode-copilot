# 题目

[242. 有效的字母异位词](https://leetcode.cn/problems/valid-anagram/)

## Copilot 解释

这段代码的目的是检查两个输入的字符串 `s` 和 `t` 是否是字母异位词。字母异位词是指两个字符串包含的字符种类和数量都相同，但顺序可以不同。

首先，创建一个长度为26的列表 `record`，用于记录每个字母在字符串 `s` 和 `t` 中出现的次数。这里26代表英文字母的数量。

然后，遍历字符串 `s`，每遇到一个字符，就在 `record` 中对应的位置上加1。这里使用 `ord(i) - ord("a")` 来找到字符在 `record` 中的位置，`ord` 函数返回字符的 ASCII 码。

`ord` 函数返回一个字符的 ASCII 码。例如，`ord("a")` 返回97，`ord("b")` 返回98，以此类推。因此，`ord(i) - ord("a")` 的结果就是字符 `i` 与 'a' 的相对距离。

例如，如果 `i` 是 'a'，那么 `ord("a") - ord("a")` 就是 0，这就是 'a' 在 `record` 中的索引位置。如果 `i` 是 'b'，那么 `ord("b") - ord("a")` 就是 1，这就是 'b' 在 `record` 中的索引位置。

接着，遍历字符串 `t`，每遇到一个字符，就在 `record` 中对应的位置上减1。这样，如果 `s` 和 `t` 是字母异位词，那么 `record` 中所有的元素都应该是0，因为 `s` 和 `t` 中每个字符出现的次数都是相同的。

最后，遍历 `record`，如果发现有非0的元素，就返回 `False`，表示 `s` 和 `t` 不是字母异位词。如果所有元素都是0，就返回 `True`，表示 `s` 和 `t` 是字母异位词。

## 复杂度

- 时间复杂度：O(n)，其中 n 是字符串 s 和 t 的长度。我们需要遍历两个字符串，每次操作的时间复杂度都是 O(1)。
- 空间复杂度：O(1)，我们只使用了一个固定大小的数组。

## Code

```py
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        for i in s:
            record[ord(i) - ord("a")] += 1
        for i in t:
            record[ord(i) - ord("a")] -= 1
        for i in range(26):
            if record[i] != 0:
                return False
        return True
```
