#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#


# @lc code=start
# 双指针；时长超出限制

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         # left, right = 0, 1
#         lens = len(numbers)
#         for i in range(lens):
#             j = i + 1
#             while j < lens:
#                 if numbers[i] + numbers[j] == target:
#                     return [i + 1, j + 1]
#                 j += 1


# 一遍哈希表
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_dict = dict()
        for idx, num in enumerate(numbers, 1):
            if target - num in num_dict:
                return [num_dict[target - num], idx]
            num_dict[num] = idx


# 有序数组，可以类似使用二分查找
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         left, right = 0, len(numbers) - 1
#         while left < right:
#             sum_ = numbers[left] + numbers[right]
#             if sum_ == target:
#                 return [left + 1, right + 1]
#             elif sum_ < target:
#                 left += 1
#             else:
#                 right -= 1


# @lc code=end

