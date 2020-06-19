#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
from typing import List


# @lc code=start
# 方法一：双指针解法
# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         nums = sorted(nums)
#         nums_len = len(nums)

#         res = []
#         for m in range(nums_len):
#             for n in range(m + 1, nums_len):
#                 left, right = n + 1, nums_len - 1
#                 while left < right:
#                     temp_res = [nums[m], nums[n], nums[left], nums[right]]
#                     if sum(temp_res) == target:
#                         left += 1
#                         right -= 1
#                         if temp_res in res:
#                             continue
#                         res.append(temp_res)
#                         # 这里需要修改指针

#                     elif sum(temp_res) > target:
#                         right -= 1
#                     else:
#                         left += 1
#                     # print(m, n, left, right)
#                     # break

#         return res


# # 方法二：双指针解法优化
# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         nums = sorted(nums)
#         nums_len = len(nums)
#         if nums_len < 4:
#             return []

#         res = []
#         for m in range(nums_len):
#             # print(m)
#             # 避免重复
#             if m > 0 and nums[m - 1] == nums[m]:
#                 continue
#             # print(m)
#             # 加入判断，判断该数组四数之和的最小值和最大值与目标值的关系
#             # 最小值大于目标值则没必要循环了
#             if (m < nums_len - 3) and sum([nums[m + i] for i in range(4)]) > target:
#                 continue
#             if sum([nums[m], nums[nums_len - 1],
#                     nums[nums_len - 2], nums[nums_len - 3]]) < target:
#                 continue

#             for n in range(m + 1, nums_len):
#                 left, right = n + 1, nums_len - 1
#                 # print(m, n, left, right)
#                 # print(n)
#                 # 避免重复
#                 if n > m + 1 and nums[n - 1] == nums[n]:
#                     continue
#                 # n同上
#                 if (n < nums_len - 2) and sum([nums[m], nums[n], nums[left], nums[n + 2]]) > target:
#                     continue
#                 if sum([nums[m], nums[n], nums[nums_len - 2],
#                         nums[right]]) < target:
#                     continue

#                 while left < right:
#                     temp_res = [nums[m], nums[n], nums[left], nums[right]]
#                     if sum(temp_res) == target:
#                         left += 1
#                         right -= 1
#                         # if temp_res in res:
#                         #     continue
#                         res.append(temp_res)
#                         # 这里需要修改指针

#                     elif sum(temp_res) > target:
#                         right -= 1
#                     else:
#                         left += 1
#                     # print(m, n, left, right)
#                     # break

#         return res


# 方法三：哈希法
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        nums.sort()
        dict_ = dict()
        res = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                sum_ = nums[i] + nums[j]
                
                # 如果两者差值在字典中，取出值
                if target - sum_ in dict_:
                    for temp in dict_[target - sum_]:
                        # 结果从小到大，防止列表重复
                        if temp[1] < i:
                            res.append(
                                (nums[temp[0]], nums[temp[1]], nums[i], nums[j])
                            )
                # 将其加入到字典中
                if sum_ not in dict_:
                    dict_[sum_] = []
                dict_[sum_].append((i, j))
        return list(set(res))


nums = [-1, 0, 1, 2, -1, -4]
target = -1
print(Solution().fourSum(nums, target))
# @lc code=end
