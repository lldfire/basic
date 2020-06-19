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
            return None
        res = sum(nums[:3])

        for k in range(nums_len):
            left = k + 1
            right = nums_len - 1
            # 循环之前加条判断
            if sum(nums[-3:]) < target:
                return sum(nums[-3:])

            if sum(nums[:3]) > target:
                return sum(nums[:3])
                
            while left < right:
                temp_res = sum([nums[k], nums[left], nums[right]])

                if abs(temp_res - target) < abs(res - target):
                    res = temp_res
                # 三数之和等于目标值时，直接返回，因为唯一
                # 三数之和大于目标值时，移动右指针
                if temp_res > target:
                    right -= 1

                elif temp_res < target:
                    left += 1
                else:
                    return res
        return res


# 这种写法能略微提升速度
# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         nums = sorted(nums)
#         nums_len = len(nums)
#         res = sum(nums[:3])

#         for k in range(nums_len):
#             left = k + 1
#             right = nums_len - 1
#             while left < right:
#                 temp_sum = sum([nums[k], nums[left], nums[right]])
#                 # 三数之和等于目标值时，直接返回，因为唯一
#                 if temp_sum == target:
#                     return temp_sum
#                 # 三数之和大于目标值时，移动右指针，记录循环终止时的点
#                 elif temp_sum > target:

#                     while (temp_sum > target) and left < right < nums_len:
#                         temp_sum = sum([nums[k], nums[left], nums[right]])
#                         right -= 1

#                 else:
#                     while (temp_sum < target) and 0 < left < right:
#                         temp_sum = sum([nums[k], nums[left], nums[right]])
#                         left += 1
 
#                 res = res if abs(res - target) < abs(temp_sum - target) else temp_sum

#         return res


nums = [-1,2,1,-4]
# k, l, r, s
# 1, 2, 128, 131
# 1, 2, 64, 67
#  

print(Solution().threeSumClosest(nums, 1))
# @lc code=end
