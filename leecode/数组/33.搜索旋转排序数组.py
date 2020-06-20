#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
from typing import List


# 可以简单理解为在数组中找到目标值的索引
# 暴力破解，不符合题意要求，应该要使用二分查找
# @lc code=start
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         if target not in nums:
#             return -1
#         return nums.index(target)


# 有序和部分有序搜索，基本都可以使用二分法查找
# 二分法
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         if not nums:
#             return -1
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             print(left, right)
#             # 找到数组中点
#             mid = (left + right) // 2
#             # 如果中点等于目标值则返回
#             if nums[mid] == target:
#                 return mid
#             # 判读左边有序还是右边有序
#             # 左边有序
#             if nums[0] <= nums[mid]:
#                 # 判断目标值在左边还是在右边
#                 # 目标值在左边
#                 if nums[0] <= target < nums[mid]:
#                     right = mid - 1
#                 else:
#                     left = mid + 1
#             # 右边有序
#             else:
#                 # 目标值在右边
#                 if nums[mid] < target <= nums[-1]:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#         return -1


# 二分法优化
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            # print(nums)
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if target >= nums[0]:
                if nums[mid] < nums[0]:
                    nums[mid] = float('inf')
            else:
                if nums[mid] >= nums[0]:
                    nums[mid] = float('-inf')

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


nums = [1, 2, 4]
print(Solution().search(nums, 1))
# @lc code=end

