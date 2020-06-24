#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
from typing import List


# @lc code=start
# 最小的正整数一定小于或等于数组长度 + 1
# 暴力法：in 方法的复杂度为 O(n),那么此法的时间复杂度就O(n^2)
# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         for i in range(0, len(nums) + 1):
#             if i + 1 not in nums:
#                 return i + 1


# 哈希表
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 基本情况
        if 1 not in nums:
            return 1
        if len(nums) == 1:
            return 2

        # 将非正数和大于len(nums) 的数改为1
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = 1

        # 最小正整数在2-lens之间。将已存在的每个值对应的索引的位置改为负数
        # 表示该值出现过
        # 与官方解所不同，这个方法的索引是从0开始
        # for i in range(len(nums)):
        #     if nums[abs(nums[i]) - 1] > 0:
        #         nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]
        #     print(nums)

        # # 找到第一个为正的索引，即没有出现的最小正数
        # for i in range(len(nums)):
        #     if nums[i] > 0:
        #         return i + 1

        # # 全为负
        # return len(nums) + 1
        for i in range(len(nums)):
            a = abs(nums[i])
            if a == len(nums):
                nums[0] = - abs(nums[0])
            else:
                nums[a] = - abs(nums[a])
            # print(nums)

        for i in range(1, len(nums)):
            if nums[i] > 0:
                return i
        
        if nums[0] > 0:
            return len(nums)

        return len(nums) + 1


nums = [2, 3, 1, 4, 6, 8, 9]
print(Solution().firstMissingPositive(nums))
# @lc code=end
