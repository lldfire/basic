#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
from typing import List


# @lc code=start
# 有序数组，使用二分查找，找到前一个值小于他，后一个值大于他的位置
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 空数组和数组中最小值比target大时
        if not nums or nums[0] >= target:
            return 0
        if nums[-1] < target:
            return len(nums)
        if nums[-1] == target:
            return len(nums) - 1

        left, right = 0, len(nums) - 1
        while left <= right:
            print(left, right)
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                # if nums[mid - 1] < target:
                #     return mid
                right = mid - 1
            else:
                # if nums[mid + 1] > target:
                #     return mid + 1
                left = mid + 1
        return left


nums = [1, 3, 5, 6]
target = 4
print(Solution().searchInsert(nums, target))
# @lc code=end
