#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#

from typing import List

# @lc code=start
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 构建字典树
        trie = dict()
        for word in words:
            curr = trie
            for w in word:
                curr = curr.setdefault(w, dict())
            curr['end'] = 1
        
        res = []
        row = len(board)
        col = len(board[0])
        def dfs():
            


words = ["oath", "pea", "eat", "rain"]
Solution().findWords([], words)
# @lc code=end

