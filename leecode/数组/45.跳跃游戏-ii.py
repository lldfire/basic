#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
from typing import List


# @lc code=start
# 方法一：反向查找找到最后一步跳跃前的位置
# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         position = len(nums) - 1
#         steps = 0
#         while position > 0:
#             for i in range(position):
#                 if nums[i] + i >= position:
#                     position = i
#                     steps += 1
#                     break
#         return steps


# 方法二：正向查找:每次查找能到达的最远位置
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step


nums = [2, 3, 1, 1, 4, 1, 2, 3, 3]
print(Solution().jump(nums))
# @lc code=end
