#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 使用集合
# class Solution:
#     def detectCycle(self, head: ListNode) -> ListNode:
#         visited = set()
#         while head:
#             if head in visited:
#                 return head
#             else:
#                 visited.add(head)
#             head = head.next
#         return None


# 双指针，两个指针相遇的节点不一定是指针入口
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        # 找到指针第一次相遇的节点
        while True:
            if not fast or not fast.next:
                return None
            slow, fast = slow.next, fast.next.next
            if fast == slow:
                break
        fast = head
        while fast != slow:
            slow, fast = slow.next, fast.next
        return fast


# @lc code=end

