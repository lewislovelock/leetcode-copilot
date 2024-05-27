# Copilot 解释

[707. 设计链表](https://leetcode.cn/problems/design-linked-list/description/)

在 `get` 方法中，我们需要获取链表中索引为 `index` 的节点的值，所以我们从 `dummy_head.next`，即链表的第一个实际节点开始遍历。

而在 `add` 方法中，我们需要在链表的某个位置插入新的节点。为了在链表的 `index` 位置插入新的节点，我们需要获取到 `index - 1` 位置的节点，然后修改它的 `next` 指针。所以我们从 `dummy_head` 开始遍历，这样当遍历结束时，`cur` 将指向 `index - 1` 位置的节点（或者在 `addAtTail` 方法中，`cur` 将指向链表的最后一个节点）。

总的来说，这两种情况下的初始设置取决于我们的目标：如果我们需要访问特定索引的节点，我们从 `dummy_head.next` 开始；如果我们需要修改特定索引节点的 `next` 指针，我们从 `dummy_head` 开始。
