#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#


# @lc code=start
# 寻找到和大于等于s的长度最小的子数组
# 暴力法
# class Solution:
#     def minSubArrayLen(self, s: int, nums: List[int]) -> int:
#         if not nums:
#             return 0
        
#         ans = len(nums) + 1
#         for i in range(len(nums)):
#             total = 0
#             for j in range(i, len(nums)):
#                 total += nums[j]
#                 if total > s:
#                     ans = min(ans, j - i)
#                     break
#         return 0 if ans == len(nums) + 1 else ans


# 双指针
# class Solution:
#     def minSubArrayLen(self, s: int, nums: List[int]) -> int:
#         if not nums:
#             return 0

#         lens = len(nums)
#         start, end = 0, 0
#         total = 0
#         ans = lens + 1

#         while end < lens:
#             total += nums[end]
#             while total >= s:
#                 ans = min(ans, end - start + 1)
#                 total -= nums[start]
#                 start += 1
#             end += 1
#         return 0 if ans == lens + 1 else ans


# 前缀和 + 双指针
# @lc code=end

