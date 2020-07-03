#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 旋转一步，将最后一个移动到第一个
# 方法一：暴力法.复杂度O(n)
# class Solution:
#     def rotateRight(self, head: ListNode, k: int) -> ListNode:
#         if k == 0:
#             return head
#         res = []
#         # print(head)
#         while head:
#             res.append(head.val)
#             head = head.next
#         if len(res) == 0:
#             return head
#         if len(res) == 1:
#             return ListNode(res[0])

#         # 旋转数组,k值太大时，旋转呈周期性变化，因此取余
#         # for i in range(k % len(res)):
#         n = k % len(res)
#         res = res[-n:] + res[:-n]
#         node = ListNode(None)
#         curr = node
#         # print(curr)
#         for val in res:
#             curr.next = ListNode(val)
#             curr = curr.next
#         curr.next = None
#         # print(node.next)
#         return node.next


# 方法二：找到断开位置，重新指定链表头和尾
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0:
            return head
        if not head:
            return None
        if not head.next:
            return head

        # 找到旧链表的尾部，使其与原链表头部相连，并统计链表长度
        n = 1
        old_node = head
        while old_node.next:
            old_node = old_node.next
            n += 1
        old_node.next = head

        # 节点断开位置 倒数第 k % n,即正数 n - k%n 此点是链表的尾部
        new_node = head
        for i in range(n - k % n - 1):
            new_node = new_node.next

        new_head = new_node.next
        new_node.next = None   # 打断链表环
        return new_head


# @lc code=end

