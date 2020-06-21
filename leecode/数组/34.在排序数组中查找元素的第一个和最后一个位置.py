#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
from typing import List


# @lc code=start
# 有序数组二分查找，注意点：target 的数量分别分0，1，2及以上时
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        if nums[0] > target or nums[-1] < target:
            return [-1, -1]

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                # 以mid为中心，向前和向后搜索
                start, end = mid, mid
                while start > left and nums[start - 1] == target:
                    start -= 1
                while end < right and nums[end + 1] == target:
                    end += 1
                return [start, end]
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return [-1, -1]


# 
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         left_idx = self.extreme(nums, target, True)
#         if left_idx == len(nums) or nums[left_idx] or nums[left_idx] != target:
#             return [-1, -1]
#         return [left_idx, self.extreme(nums, target, False) - 1]
    
#     def extreme(self, nums, target, left):
#         lo = 0
#         hi = len(nums)

#         while lo < hi:
#             mid = (lo + hi) // 2
#             # 在左半部分
#             if nums[mid] > target or (left and target == nums[mid]):
#                 hi = mid
#             else:
#                 lo = mid + 1
#         # 返回左索引
#         return lo


nums = [5]
target = 5
print(Solution().searchRange(nums, target))
# @lc code=end
