from typing import List
from collections import defaultdict
from functools import reduce


# words = ["w", "wo", "wor", "worl", "world"]
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]


# # 方法一：暴力破解
# class Solution:
#     def longestWord(self, words: List[str]) -> str:
#         wordset = set(words)
#         # 根据单词的长度进行排序，长的排在前
#         words.sort(key=lambda c: (len(c), c), reverse=True)
#         print(words)
#         # 判断字符串的每个字符是否在字典中
#         for word in words:
#             if all(word[:k] in wordset for k in range(1, len(word))):
#                 return word
#         else:
#             return ''


# 方法二：前缀树+深度优先
class Solution:
    def longestWord(self, words: List[str]) -> str:
        Trie = lambda: defaultdict(Trie)
        trie = Trie()
        END = True

        for i, word in enumerate(words):
            reduce(dict.__getitem__, word, trie)[END] = i
        # print(dict(trie).values())
        stack = list(trie.values())
        ans = ''
        while stack:
            print(stack)
            cur = stack.pop()

            # END在树中，说明这是一个词的开始
            if END in cur:
                word = words[cur[END]]
                # print(word)
                if len(word) > len(ans) or len(ans) or len(word) == len(ans) and word < ans:
                    ans = word
                stack.extend([cur[letter] for letter in cur if letter != END])
        return ans


        

print(Solution().longestWord(words))
