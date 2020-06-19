#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#
from typing import List


# @lc code=start
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         while val in nums:
#             nums.remove(val)
#         return len(nums)


# 双指针解法
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         if len(nums) == 0:
#             return 0
#         i = 0
#         for j in range(len(nums)):
#             if nums[j] != val:
#                 nums[i] = nums[j]
#                 i += 1
#         return i


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        tag = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            # print(tag, i)
            if nums[i] == val:
                # print(nums[i], nums[tag])
                nums[i], nums[tag] = nums[tag], nums[i]
                tag -= 1
        return tag + 1


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
Solution().removeElement(nums, val)
# @lc code=end
