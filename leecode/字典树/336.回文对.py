#
# @lc app=leetcode.cn id=336 lang=python3
#
# [336] 回文对
#
from typing import List


# @lc code=start
# 方法一：先试用暴力法，加深题目理解
# class Solution:
#     def palindromePairs(self, words: List[str]) -> List[List[int]]:
#         res = []
#         for i, w1 in enumerate(words):
#             for j, w2 in enumerate(words):
#                 if i == j:
#                     continue
#                 word_comb = w1 + w2
#                 if word_comb == word_comb[::-1]:
#                     res.append([i, j])
#         return res


# @lc code=start
# 方法二：字典树
class TrieNode:
    def __init__(self):
        self.Node = dict()
        self.index = -1   # 当前单词的索引
        self.word = None

    def insert(self, word, index):
        curr = self
        # 单词的逆序加入字典数中
        for char in word[::-1]:
            if char not in curr.Node:
                curr.Node[char] = TrieNode()
            curr = curr.Node[char]
        curr.index = index
        curr.word = word


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = TrieNode()
        for i, word in enumerate(words):
            trie.insert(word, i)
        # print(trie.Node['d'].Node['c'].word)
        # print(trie.Node['s'].index)
        # print(trie.Node['s'].word)

        


words = ["abcd", "dcba", "lls", "s", "sssll"]

Solution().palindromePairs(words)