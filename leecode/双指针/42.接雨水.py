#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# 双指针
# @lc code=start
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         lens = len(height)
#         if lens <= 2:
#             return 0
#         left, right = 0, lens - 1
#         left_max, right_max = 0, 0
#         res = 0
#         while left < right:
#             if height[left] <= height[right]:
#                 if height[left] >= left_max:
#                     left_max = height[left]
#                 else:
#                     res += left_max - height[left]
#                 left += 1
#             else:
#                 if height[right] >= right_max:
#                     right_max = height[right]
#                 else:
#                     res += right_max - height[right]
#                 right -= 1
#         return res


# 栈
class Solution:
    def trap(self, height: List[int]) -> int:
        lens = len(height)
        if lens <= 2:
            return 0
        
        res = 0
        curr = 0
        stack = []
        while curr < lens:
            # 出栈条件
            # 指针上的元素大于栈顶元素，说明可以装雨水
            while stack and height[curr] > height[stack[-1]]:
                h = height[stack.pop()]
                if not stack:
                    break
                dis = curr - stack[-1] - 1
                min_ = min(height[curr], height[stack[-1]])
                res += (min_ - h) * dis
            stack.append(curr)
            curr += 1
        return res

# @lc code=end

