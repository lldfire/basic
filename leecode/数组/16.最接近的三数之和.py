#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
from typing import List


# @lc code=start
# 排序双指针，计算三数之和后再计算与目标数的差值，差值最小即最接近，
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        nums_len = len(nums)
        if nums_len < 3:
            return []
        # res = None
        for k in range(nums_len):
            left = k + 1
            right = nums_len - 1
            while left < right:
                temp_list = [nums[k], nums[left], nums[right]]
                # 三数之和等于目标值时，直接返回，因为唯一
                if sum(temp_list) == target:
                    return temp_list
                # 三数之和大于目标值时，移动右指针
                # 移动后的三数之和大于与移动前的三数之和比较

                # 三数之和小于目标值时，移动左指针
# @lc code=end

