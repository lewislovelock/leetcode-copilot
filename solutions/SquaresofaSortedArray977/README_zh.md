# Copilot 解释

这个算法的主要思想是利用双指针技术。由于数组是非递减排序的，所以数组的平方可能会在数组的两端产生最大值。因此，我们使用两个指针，一个指向数组的开始（左指针），另一个指向数组的结束（右指针）。

然后，我们比较两个指针指向的数的平方，将较大的那个数的平方放入结果数组的最后一个位置，并将对应的指针向中间移动。这样，我们就能保证结果数组是按非递减顺序排序的。

这个过程会一直持续到左指针和右指针相遇，这时我们就处理完了所有的元素。

## 复杂度

- 时间复杂度：O(n)，因为我们只遍历了一次数组，这里的 n 是数组的长度。
- 空间复杂度：O(n)，我们创建了一个新的数组来存储结果，这个数组的大小与输入数组的大小相同。

## 代码

```py
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        >>> Solution().sortedSquares([-4,-1,0,3,10])
        [0,1,9,16,100]
        >>> Solution().sortedSquares([-7,-3,2,3,11])
        [4,9,9,49,121]
        """
        i, j, k = 0, len(nums)-1, len(nums)-1
        res = [0] * len(nums)
        while i <= j:
            if nums[i]**2 < nums[j]**2:
                res[k] = nums[j]**2
                j -= 1
            else:
                res[k] = nums[i]**2
                i += 1
            k -= 1
        return res
```
