#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#


# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        left, right = 0, len(s_list) - 1
        aeiou = ['a', 'e', 'i', 'o', 'u']
        while left < right:
            # 左指针是否是元音字母
            while left < right and s_list[left].lower() not in aeiou:
                left += 1
            while left < right and s_list[right].lower() not in aeiou:
                right -= 1
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
    
        return ''.join(s_list)

# @lc code=end

