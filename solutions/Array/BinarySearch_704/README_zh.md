# Copilot 解释

这段代码实现的是二分查找算法，它是一种在有序数组中查找特定元素的搜索算法。

首先，我们定义两个指针 `left` 和 `right`，分别指向数组的开始和结束。这两个指针定义了一个搜索区间。

然后，我们进入一个循环，只要 `left` 不大于 `right`，我们就继续搜索。

在每次循环中，我们首先计算 `middle`，它是 `left` 和 `right` 的中点。这里的计算方式 `left + (right - left) // 2` 是为了防止 `(left + right) // 2` 造成的溢出。当 `left` 和 `right` 都很大的时候，`left + right` 可能会超过整数的最大值，导致溢出。而 `left + (right - left) // 2` 则不会有这个问题。

接下来，我们比较 `middle` 位置的元素和目标值 `target`。如果 `middle` 位置的元素大于 `target`，那么 `target` 应该在 `middle` 的左边，所以我们将 `right` 移动到 `middle - 1`。如果 `middle` 位置的元素小于 `target`，那么 `target` 应该在 `middle` 的右边，所以我们将 `left` 移动到 `middle + 1`。如果 `middle` 位置的元素等于 `target`，那么我们就找到了 `target`，直接返回 `middle`。

如果循环结束还没有找到 `target`，那么就返回 `-1`，表示 `target` 不在数组中。

## 复杂度

- 时间复杂度：时间复杂度为 O(log n)，因为我们每次比较都会将输入的大小减半。这里的 n 是数组的长度。

- 空间复杂度：空间复杂度为 O(1)，因为我们没有使用与输入大小成比例的额外空间。我们只使用了恒定的空间来存储指针。

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
