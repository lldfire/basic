#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#


# @lc code=start
# 双指针
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        [4,2,4,0,0,3,0,5,1,0]
        """
        if len(nums) < 2:
            return nums
        # 方法1：
        # i, j = 0, 0
        # while j < len(nums):
        #     if nums[j] == 0:
        #         j += 1
        #     else:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         i += 1
        #         j += 1

        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        
        # 方法二：
        # 遇到0就删除，并在尾部补上0
        # i = 0
        # n = 0
        # while i < len(nums):
        #     if nums[i] == 0:
        #         n += 1
        #         nums.pop(i)
        #         nums.append(0)
        #     else:
        #         i += 1
        #     n += 1
        #     if n + i > len(nums):
        #         break

        return nums


# @lc code=end

