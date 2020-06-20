#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
from typing import List


# @lc code=start
class Solution:
    def insertion_sort(self, start, nums):
        """
        对start索引之后的数据进行插入排序
        """
        for i in range(start, len(nums)-1):
            num, idx = nums[i+1], i
            # 判断第 i+1 个数是否小于 第 i 个数，如果是则
            while start <= idx and num < nums[idx]:
                nums[idx+1] = nums[idx]
                idx -= 1
            nums[idx+1] = num
        return nums

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums

        start = len(nums) - 1
        while start > 0:
            # 从列表右边向前查找元素，当此数比他前一个数大时退出循环
            if nums[start] > nums[start - 1]:
                break
            start -= 1

        # 如果 start == 0说明该排列已经是最大的一个排列，将数组逆序输出
        if start == 0:
            return self.insertion_sort(0, nums)
        # 优化此处代码，在start = 0 时，数组是一个降序排列的数组，
        # 使用双指针进行首尾位置数据互换
        # if start == 0:
        #     l, r = 0, len(nums) - 1
        #     while l < r:
        #         nums[l], nums[r] = nums[r], nums[l]
        #         l += 1
        #         r -= 1

        # 找到 start 之后的数中比 nums[start - 1]大的最小的数，并与之交换位置
        # min_num = nums[start]
        # min_idx = start
        # for s in range(start, len(nums)):
        #     if nums[s] > nums[start - 1] and nums[s] < min_num:
        #         min_num = nums[s]
        #         min_idx = s

        # 优化以上代码，从start 往后的数据是降序排列，因此可以从后往前查找
        for min_idx in range(len(nums) - 1, start - 1, -1):
            if nums[min_idx] > nums[start - 1]:
                break
        nums[start - 1], nums[min_idx] = nums[min_idx], nums[start - 1]

        # 对start 之后的数字排序
        return self.insertion_sort(start, nums)


nums = [6, 1, 2, 4, 3, 0]
# nums = [6, 5, 4, 3, 2, 1]

# print(Solution().insertion_sort(nums))
print(Solution().nextPermutation(nums))
# @lc code=end
