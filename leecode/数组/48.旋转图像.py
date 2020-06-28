#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#
from typing import List


# @lc code=start
# # 方法一：先转置矩阵，再翻转每一行
# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         lens = len(matrix)
#         for i in range(lens):
#             for j in range(i, lens):
#                 matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

#         for i in range(lens):
#             matrix[i].reverse()
# print(matrix)


# 方法二：逐层旋转
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        start, end = 0, len(matrix) - 1
        while start < end:
            for add in range(end - start):
                # 取出一块数据临时存储
                temp = matrix[end - add][start]
                matrix[end - add][start] = matrix[end][end - add]
                matrix[end][end - add] = matrix[start + add][end]
                matrix[start + add][end] = matrix[start][start + add]
                matrix[start][start + add] = temp
            start += 1
            end -= 1
        # for i in range(len(matrix)):
        #     for j in range(i, len(matrix)):

        # print(matrix)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
Solution().rotate(matrix)
# @lc code=end
