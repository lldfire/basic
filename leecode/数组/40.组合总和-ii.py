#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
from typing import List


# @lc code=start
# 回溯算法，与上一题类似，所不同的是，每个元素只能使用一次
# 如何剪枝，避免重复呢
# 1.上一节点已经使用过的元素不再使用
# 
# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         res = []
#         path = []
#         lens = len(candidates)
#         candidates.sort()
#         self.__dfs(path, target, res, candidates, lens)
#         return res

#     def __dfs(self, path, target, res, candidates, lens, beg=0):
#         """
#         :param path:  递归找到的最优的树
#         """
#         # 结束条件
#         if sum(path) == target:
#             res.append(path[:])
#             return

#         for n in range(beg, lens):
#             print(path)
#             # 剪枝，当所求路径的和大于目标值时停止搜索
#             if sum(path) > target:
#                 break

#             # 增加剪枝，避免组合重复
#             # 即当前分支和上一个分支相同时，减掉
#             if n > beg and candidates[n - 1] == candidates[n]:
#                 continue
#             path.append(candidates[n])
#             # 剪枝，从n+1开始，避免同一个元素被多次引用
#             self.__dfs(path, target, res, candidates, lens, n + 1)
#             path.pop()


# 回溯搜索减法
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        lens = len(candidates)
        candidates.sort()
        self.__dfs(path, target, res, candidates, lens)
        return res

    def __dfs(self, path, target, res, candidates, lens, beg=0):
        """
        :param path:  递归找到的最优的树
        """
        # 结束条件
        if target == 0:
            res.append(path[:])
            return

        for n in range(beg, lens):
            chazhi = target - candidates[n]
            # 剪枝，当所求路径的和大于目标值时停止搜索
            if chazhi < 0:
                break

            # 增加剪枝，避免组合重复
            # 即当前分支和上一个分支相同时，减掉
            if n > beg and candidates[n - 1] == candidates[n]:
                continue
            path.append(candidates[n])
            # 剪枝，从n+1开始，避免同一个元素被多次引用
            self.__dfs(path, chazhi, res, candidates, lens, n + 1)
            path.pop()


candidates = [2, 5, 2, 1, 2]
target = 5
print(Solution().combinationSum2(candidates, target))
# @lc code=end
