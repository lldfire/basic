#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
from typing import List


# @lc code=start
# 递归回溯
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         candidates.sort()
#         lens = len(candidates)
#         res = []
#         path = []

#         self.__dfs(res, candidates, lens, path, target)
#         return res

#     def __dfs(self, res, candidates, lens, path, target, beg=0):
#         """
#         回溯算法，深度搜索
#         """
#         if target == 0:
#             res.append(path[:])
#             return

#         for idx in range(beg, lens):
#             cha = target - candidates[idx]
#             if cha < 0:
#                 # 因为是有序数组，所有直接break，否则continue
#                 break
#             # 向路径中添加选择
#             path.append(candidates[idx])
#             # 有重复值需要进行剪枝，即递归搜索中从index往后搜索，不再从头搜索
#             self.__dfs(res, candidates, lens, path, cha, idx)
#             # 回溯
#             path.pop()


# # 回溯算法框架
# # result = []
# # def backtrack(路径, 选择列表):
# #     if 满足结束条件:
# #         result.add(路径)
# #         return

# #     for 选择 in 选择列表:
# #         做选择
# #         backtrack(路径, 选择列表)
# #         撤销选择

# # class Solution:
# #     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
# #         print(candidates)
# #         if target < 0 or len(candidates) <= 0:
# #             return []
# #         if target == 0:
# #             return [[]]
# #         return self.combinationSum(candidates[1:], target) + \
# #             [[candidates[0]] +
# #                 cp for cp in self.combinationSum(candidates, target - candidates[0])]


# candidates = [2, 3, 6, 7]
# target = 7
# print(Solution().combinationSum(candidates, target))
# @lc code=end

# 全排列帮助理解回溯算法
class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        def trackBack(nums, track, lens, beg=0):
            # print(track)
            if len(track) == len(nums):
                res.append(track[:])  
                # 需要传递下track的拷贝，否则对track的修改会影响到结果
                return
            for i in range(beg, nums):
                if nums[i] in track:
                    continue
                # print('递归前', track)
                track.append(nums[i])
                trackBack(nums, track, lens, i)
                # print('递归后', track)
                track.pop()
                # print('撤销后', track)
                # break
        res = []
        track = []
        lens = len(nums)
        trackBack(nums, track, lens)
        return res


# Solution().permute([1, 2, 3])