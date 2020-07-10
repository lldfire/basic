#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#
from collections import Counter


# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 方法一：hash表
        # nums1_count = Counter(nums1)
        # nums2_count = Counter(nums2)
        # res = []
        # for num in nums1_count:
        #     if num in nums2_count:
        #         res += [num] * min(nums1_count[num], nums2_count[num])
        # return res

        # 方法二：排序 + 双指针
        nums1.sort()   # 排序
        nums2.sort()
        i, j = 0, 0
        res = list()
        while i < len(nums1) and j < len(nums2):
            # 如果num1 小于num2 增大num1,寻找更接近值，
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                j += 1
                # k += 1
                i += 1
        return res
                

# @lc code=end

