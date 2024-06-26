# Copilot 解释

首先，我们创建一个新的列表 `res`，它是 `nums` 的副本。然后我们创建一个空的哈希表 `hash`。

然后，我们对 `res` 进行排序。排序后的 `res` 列表中，每个元素的索引就是比它小的元素的数量。例如，如果 `res` 是 `[1,2,2,3,8]`，那么数字 `1` 的索引是 `0`，表示没有比 `1` 小的数字；数字 `2` 的索引是 `1`，表示有一个比 `2` 小的数字，即 `1`。

接下来，我们遍历排序后的 `res`，并将每个元素和它的索引添加到哈希表 `hash` 中。如果遇到相同的数字，我们不更新哈希表，因为我们只关心第一次出现的索引，这是因为我们想要的是比当前数字小的数字的数量，而不是等于当前数字的数量。

最后，我们再次遍历原始的 `nums` 列表，并使用哈希表 `hash` 来查找每个元素的索引，然后将这个索引值赋给 `res` 中对应的位置。这样，`res` 中的每个元素就变成了比原始 `nums` 中对应位置的元素小的元素的数量。

最后返回 `res`，就得到了我们想要的结果。

## 复杂度

- 时间复杂度：时间复杂度为 O(n log n)，因为我们正在对数组进行排序。这里的 n 是数组的长度。

- 空间复杂度：空间复杂度为 O(n)，因为我们使用了一个与输入数组大小相同的额外数组和一个哈希表来存储计数。在最坏的情况下，哈希表的大小可以等于数组的大小。

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
