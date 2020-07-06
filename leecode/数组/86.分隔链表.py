#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 双指针
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 创建哑链表
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)
        while head:
            # print(before_head)
            # 小于x的置于before中
            if head.val < x:
                before.next = head
                before = before.next
            # 大于x的置于after中
            else:
                # print(2, after)
                after.next = head
                after = after.next
            head = head.next
        after.next = None
        before.next = after_head.next
        return before_head.next

# @lc code=end

