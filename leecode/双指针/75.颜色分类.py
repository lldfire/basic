#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#


# @lc code=start
# 方法一：计数
# 方法二：维护三个指针，
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, p1, p2 = 0, 0, len(nums) - 1
        while p1 <= p2:
            # 等于 0 时，与p0交换，并更新p0, p1
            if nums[p1] == 0:
                nums[p0], nums[p1] = nums[p1], nums[p0]
                p0 += 1
                p1 += 1
            # 等于 1 时，p1后移
            elif nums[p1] == 1:
                p1 += 1
            elif nums[p1] == 2:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p2 -= 1

        
# @lc code=end
