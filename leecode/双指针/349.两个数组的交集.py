#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#


# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 元素唯一，集合，减少遍历量
        # 方法一：使用内置函数
        # return set(nums1).intersection(set(nums2))

        # 方法二：使用集合运算符
        # return list(set(nums1) & set(nums2))

        # 方法三：in 方法
        # return [num for num in set(nums1) if num in set(nums2)]

        # 方法四：使用额外空间，查找
        # nums = list(set(nums1)) + list(set(nums2))
        # nums.sort()
        # res = []
        # for i in range(1, len(nums)):
        #     if nums[i - 1] == nums[i]:
        #         res.append(nums[i])
        # return res

# @lc code=end
