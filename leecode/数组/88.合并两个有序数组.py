#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
# 双指针，从前往后
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         nums1_copy = nums1[:m]
#         nums1[:] = []
#         i = 0
#         j = 0
#         while i < m and j < n:
#             if nums1_copy[i] < nums2[j]:
#                 nums1.append(nums1_copy[i])
#                 i += 1
#             else:
#                 nums1.append(nums2[j])
#                 j += 1
#         if i < m:
#             nums1[i+j:] = nums1_copy[i:]
#         if j < n:
#             nums1[i+j:] = nums2[j:]


# 双指针，从后往前
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        p = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[p] = nums1[i]
                i -= 1
            else:
                nums1[p] = nums2[j]
                j -= 1
            p -= 1
        nums1[:j + 1] = nums2[:j + 1]

# @lc code=end
