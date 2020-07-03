#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除排序数组中的重复项 II
#
from typing import List


# 有序数组, 把多余的数放到最后，那最后面，并把最后面的数取出来，备用
# @lc code=start
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         # 遍历数组，并对每个元素进行计数
#         i, count = 1, 1
#         while i < len(nums):
#             # 如果当前元素等于前一个元素，则count + 1,
#             if nums[i] == nums[i - 1]:
#                 count += 1
#                 # 如果count 大于 2移除该索引元素，同时索引-1
#                 if count > 2:
#                     nums.pop(i)
#                     i -= 1
#             # 如果当前元素和前一个元素不等，count等于1
#             else:
#                 count = 1
#             i += 1
#         return len(nums)


# 双指针，覆盖元素
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j, count = 1, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1
            if count <= 2:
                nums[j] = nums[i]
                j += 1
        return j
        
# @lc code=end

