#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 回文链表,将链表中的值复制到列表中，再判断列表是否为回文
# 空间复杂度不符合要求
# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         if not head:
#             return True
        
#         head_list = []
#         while head:
#             head_list.append(head.val)
#             head = head.next
        
#         l, r = 0, len(head_list) - 1
#         while l < r:
#             if head_list[l] != head_list[r]:
#                 return False
#             l += 1
#             r -= 1
#         return True


# 快慢指针,fast is None 链表节点数为奇数，fast.next is None 链表节点数为偶数
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 边界情况
        if not head or not head.next:
            return True
        recnct, slow, fast = head, head, head
        newhead = None

        while fast and fast.next:
            fast = fast.next.next
            temp = slow
            # print(temp)
            slow = slow.next
            temp.next = newhead
            newhead = temp
            # print(temp, newhead)
            
        recnct.next = slow
        ps = newhead
        pf = slow.next if fast else slow
        while pf:
            if ps.val != pf.val:
                return False
            ps = ps.next
            pf = pf.next
        return True
    
# @lc code=end

