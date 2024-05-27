# 题目

[202. 快乐数](https://leetcode.cn/problems/happy-number/description/)

## Copilot 解释

这段代码的目标是判断一个数字是否是"快乐数"。一个"快乐数"定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，或者无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。

首先，我们创建一个集合 `visited` 来存储已经访问过的数字，防止无限循环。

然后，我们进入一个循环，条件是 `n` 不等于 1 并且 `n` 还没有被访问过。在循环中，我们首先把 `n` 添加到 `visited` 中，然后把 `n` 更新为它每个位置上的数字的平方和。

最后，如果 `n` 变为了 1，我们返回 True，表示它是一个快乐数。如果 `n` 无法变为 1，我们返回 False。

## 复杂度

- 时间复杂度：O(logn)，其中 n 是输入的数字。因为每一次操作都会使 `n` 变小，所以时间复杂度是对数级别的。
- 空间复杂度：O(logn)，我们需要一个集合来存储已经访问过的数字，最坏情况下，这个集合的大小和输入的数字的位数相同，所以空间复杂度也是对数级别的。

## Code

```py
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
        return n == 1
```
