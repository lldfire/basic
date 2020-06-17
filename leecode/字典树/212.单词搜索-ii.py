#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#

from typing import List


# @lc code=start
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 将所有单词依次填入字典树中
        trie = dict()
        # curr = trie
        for word in words:
            curr = trie
            for w in word:
                curr = curr.setdefault(w, dict())
            curr['end'] = 1

        res = []
        rows = len(board)
        cols = len(board[0])

        def dfs(row, col, trie, str_):
            char = board[row][col]
            if char not in trie:
                return
            print(char)
            curr = trie[char]
            if 'end' in curr and curr['end'] == 1:
                res.append(str_ + char)
                curr['end'] = 0

            board[row][col] = '#'    # 标志位，防止重复搜索，后面会改回来
            # 向上下左右四个方向搜索
            for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                temp_row = row + x
                temp_col = col + y
                if 0 <= temp_row < rows and 0 <= temp_col < cols and board[temp_row][temp_col] != '#': 
                    dfs(temp_row, temp_col, curr, str_ + char)
            board[row][col] = char
        
        for row in range(rows):
            for col in range(cols):
                dfs(row, col, trie, '')
        return res


# 方法二：将board加入到字典树中，搜索单词列表，理论上极耗内存
# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         trie = dict()
#         rows = len(board)
#         cols = len(board[0])
#         for row in range(rows):
#             for col in range(cols):
#                 char = board[row][col]
#                 curr = curr.setdefault(char, dict())
#         print(trie)


board = [
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
]

words = ["oath", "pea", "eat", "rain", "orange"]
print(Solution().findWords(board, words))
# @lc code=end
