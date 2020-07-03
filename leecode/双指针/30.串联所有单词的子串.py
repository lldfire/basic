#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#
from typing import List
from collections import Counter


# @lc code=start
# 所有单词都要参与其中，顺序无所谓
# words中的单词长度相同，
# 串联的方式，n!中单词组合方式
# 方式一：hashmap,将words中的每个单词都存入到字典中
# class Solution:
#     def findSubstring(self, s: str, words: List[str]) -> List[int]:
#         if not words or not s:
#             return []
#         res = []
#         words_len = len(words)
#         str_len = words_len * len(words[0])
#         # 将words中的单词添加到词典中去
#         words_dict = Counter(words)

#         # 依次截取words所有单词长度和长的字符串
#         for i in range(len(s) - str_len + 1):
#             temp_word = s[i: i + str_len]
#             temp_list = []
#             # 将截取的字符串按每个单词的长度分割并加入列表中
#             for j in range(0, str_len, len(words[0])):
#                 temp_list.append(temp_word[j:j + len(words[0])])
#             # 统计词频后与words进行比较
#             if Counter(temp_list) == words_dict:
#                 res.append(i)
#         return res


# 方法二：双指针
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        left, right = 0, 0
        lens = len(words[0])
        wordsdict = Counter(words)
        res = []

        for i in range(lens):
            # 从不同位置开始，保证将所有的可能组合都遍历到
            left, right = i, i
            cnt = 0    # 以匹配到的单词的数量
            curr_dict = Counter()
            
            # left 最远位置
            while left <= len(s) - lens * len(words):
                while cnt < len(words):
                    # 右指针右移，截取单词
                    curr_str = s[right:right + lens]
                    # words中没有该字符串
                    if curr_str not in wordsdict:
                        break
                    # 截取区间内单词的数量大于words中的数量
                    elif curr_str in curr_dict and curr_dict[curr_str] + 1 \
                        > wordsdict[curr_str]:
                        break

                    curr_dict[curr_str] += 1
                    cnt += 1
                    right += lens

                if curr_dict == wordsdict:
                    res.append(left)
                
                # 以下两个判断的是while循环跳出的两个情况
                # 如果words中没有当前单词
                if curr_str not in wordsdict:
                    # 更新右指针继续查询下一个单词，并更新左指针
                    while right + lens <= len(s) and s[right: right + lens]\
                        not in wordsdict:
                        right += lens
                    left = right
                    cnt = 0
                    curr_dict = Counter()
                
                else:
                    if curr_dict[curr_str] > wordsdict[curr_str]:
                        # 左指针右移，直到右移后的单词等于当前单词时
                        while left + lens <= len(s) - lens * len(words) and \
                            s[left:left + lens] != curr_str:
                            left += lens
                    # 从当前词典中减-1，以便下一轮循环
                    curr_dict[s[left:left + lens]] = curr_dict[s[left:left \
                        + lens]] - 1
                    cnt = cnt - 1
                    left += lens
        return res
# @lc code=end
