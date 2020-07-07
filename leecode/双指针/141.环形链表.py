#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 集合算法，复杂度o(n)，将每个节点都保存在集合中，如果当前节点为None,则表示已到集合尾部
# 说明不是环形链表，如果当前链表存在于集合中，那说明是环形链表
# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         hashs = set()
#         while head:
#             if head in hashs:
#                 return True
#             else:
#                 hashs.add(head)
#             head = head.next
#         return False


# 快慢指针算法，因为是环形链表，快慢指针总会有相遇的那一刻
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 空链表或者只有一个节点时
        if not head or not head.next:
            return False

        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        
        return True


# @lc code=end

