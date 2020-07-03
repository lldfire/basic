#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
from collections import Counter


# @lc code=start
# 不包含字符串，右指针右移，包含字符串左移
# 维护一个词典，判断窗口中是否包含该
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''

        t_dict = Counter(t)    # 统计t中每个单词出现的次数
        t_len = len(t)         # t的长度
        left = 0    # 慢指针
        res = (0, len(s) + 1)

        for right, char in enumerate(s):
            # 通过更改t_len的方式来判断是否找到次优解
            if t_dict[char] > 0:
                t_len -= 1
            # print(t_dict)
            # 判断字符中是否包含目标字符串
            t_dict[char] -= 1
            
            if t_len == 0:
                while 1:
                    # 直到出现t中的某个字母时，结束增加left，并向hash中增加该字母
                    # 然后移动right直到找到下一个该字母
                    if t_dict[s[left]] == 0:
                        break
                    t_dict[s[left]] += 1
                    left += 1
                # 更新结果
                if right - left < res[1] - res[0]:
                    res = (left, right)
                # 
                t_dict[s[left]] += 1
                t_len += 1
                left += 1
                
        return '' if res[1] == len(s) + 1 else s[res[0]:res[1] + 1]

        
# @lc code=end

