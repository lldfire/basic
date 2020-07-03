#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 方法一： 两次遍历，第一次遍历取出链表中的元素,并删除倒数第n个，
# 第二次遍历得到一个新的链表
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None

        stacks = []
        # 取出链表中的所有内容
        while head:
            stacks.append(head)
            head = head.next
        # 删除链表中第n个元素
        print(stacks)
        stacks.pop(-n)
        new_ = ListNode(0)
        d1 = new_
        # 将剩余元素组成新的链表并返回
        for i in range(len(stacks)):
            d1.next = stacks[i]
            d1 = d1.next
        d1.next = None
        return new_.next


# 方法二: 两次遍历，第一次遍历得到链表的长度L，第二次遍历删除 L-n的元素
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         dummy = ListNode(0)
#         dummy.next = head   # 起到占位置的作用，
#         print(dummy)
#         lens = 0
#         first = head
#         while first:
#             lens += 1
#             first = first.next
#         # 找到地要被删除的节点
#         lens -= n
#         # 碰到该元素后跳过
#         first = dummy
#         while lens > 0:
#             lens -= 1
#             first = first.next
#         first.next = first.next.next
#         return dummy.next


# # 方法三:双指针快指针领先 n 步，然后同时动，快指针无法移动时，移出慢指针的元素
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         # 定义一个头节点
#         node = ListNode(None)
#         node.next = head
#         # 快慢指针
#         fast, slow = node, node
#         # 领先n步
#         for _ in range(n):
#             fast = fast.next
#         # 快指针到达尾部时，慢指针达到倒数第n个的前一个
#         while fast.next:
#             fast = fast.next
#             slow = slow.next
#         slow.next = slow.next.next
#         return node.next


# @lc code=end
