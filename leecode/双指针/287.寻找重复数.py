#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#


# @lc code=start
# 数组只读，意味着不能使用排序
# 否则使用排序，一遍遍历
# 限制了数据空间，否则使用hash表，一遍遍历
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 方法一：暴力破解.超时
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return nums[i]

        # 方法二：hash表，不符合空间复杂度
        # nums_dict = dict()
        # for num in nums:
        #     if num in nums_dict:
        #         return num
        #     nums_dict[num] = 
        
        # 方法三：排序后一遍遍历，不符合数组只读
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i - 1] == nums[i]:
        #         return nums[i]
        
        # 方法四:双指针，快慢指针
        # 将元素视为数组的索引，然后使用快慢指针，寻找到环的入口
        slow, fast = 0, 0
        while 1:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # slow = fast 是相遇点，不是重复值点，
        # 环的入口才是重复值点，参看环形链表-ii

        find = 0
        while 1:
            find = nums[find]
            slow = nums[slow]
            if slow == find:
                return slow

        # 方法5:二分查找，需要额外使用空间

        
# @lc code=end
