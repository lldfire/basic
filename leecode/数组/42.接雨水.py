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
# 在方法一中要每次都要向前向后便利找到最大值
# 动态规划则提出提前保存位置i之前之后的最大值
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         if not height:
#             return 0

#         res = 0
#         lens = len(height)
#         left_max = dict()
#         right_max = dict()
#         left_max[0] = height[0]
#         # 找到数组中从下标 i 到最左端最高的条形块高度 left_max
#         for i in range(1, lens):
#             # 存储位置I左边的最大值
#             left_max[i] = max(left_max[i - 1], height[i])
#         # 找到数组中从下标 i 到最右端最高高度
#         right_max[lens - 1] = height[-1]
#         for i in range(lens - 2, -1, -1):
#             right_max[i] = max(right_max[i + 1], height[i])
#         for i in range(lens):
#             res += min(left_max[i], right_max[i]) - height[i]
#         return res


# 方法四：栈的应用
class Solution:
    def trap(self, height: List[int]) -> int:
        lens = len(height)
        if lens < 3:
            return 0
        
        res = 0
        stack = []
        curr = 0
        while curr < lens:
            # 栈不空，且当前元素大于栈顶（栈中最后一个元素）元素
            while len(stack) != 0 and height[curr] > height[stack[-1]]:
                # 将要出栈的元素
                h = height[stack.pop()]
                # 栈空时就退出去
                if len(stack) == 0:
                    break
                # 两堵墙之间的距离
                distance = curr - stack[-1] - 1
                min_ = min(height[curr], height[stack[-1]])

                res += distance * (min_ - h)
            stack.append(curr)
            curr += 1
        return res

# 方法五：双指针
# 在方法三中，发现当left_max < right_max时，积水值由左侧决定，反之亦然
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         lens = len(height)
#         if lens <= 1:
#             return 0

#         res = 0
#         left, right = 0, lens - 1
#         left_max, right_max = 0, 0

#         while left < right:
#             if height[left] < height[right]:
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


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution().trap(height))

# @lc code=end
