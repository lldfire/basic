#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
from typing import List


# @lc code=start
# 方法一：暴力法，按列求；
# 核心思想：遍历每一个元素，从当前元素（包含）开始向前和向后
# 找到当前元素（包含）之前和之后的两个最大值中较小的一个 减去当前元素的高
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         res = 0
#         for i in range(1, len(height) - 1):
#             print('索引', i)
#             left, right = 0, 0
#             for j in range(i, -1, -1):
#                 left = max(left, height[j])
#             for k in range(i, len(height)):
#                 right = max(right, height[k])
#             print(left, right)
#             res += min(left, right) - height[i]
#             print('结果', res)
#         return res


# 方法二：按行遍历，共3行,超时哈哈哈哈哈
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         if not height:
#             return 0
#         lens = len(height)
#         max_ = max(height)
#         res = 0

#         for i in range(1, max_ + 1):
#             temp = 0
#             flag = False
#             for j in range(1, lens - 1):
#                 if height[j] < i and flag:
#                     temp += 1
#                 if height[j] >= i:
#                     res += temp
#                     temp = 0
#                     flag = True
#             print(res)
#         return res


# 方法三：动态规划法
# 在方法一中要
class Solution:
    def trap(self, height: List[int]) -> int:
        pass


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution().trap(height))

# @lc code=end
