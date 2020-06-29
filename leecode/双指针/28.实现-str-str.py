#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#


# @lc code=start
# 方法一：使用字符串的index方法
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         try:
#             return haystack.index(needle)
#         except Exception:
#             return -1


# 方法二：双指针
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 空字符串返回 0
        if not needle:
            return 0
        
        hlen, nlen = len(haystack), len(needle)
        if nlen > hlen:
            return -1

        ph = 0
        while ph < hlen - nlen + 1:
            # 指针ph小于字符产的长度，且所指位置不等于needle的首字母时，继续增加
            while ph < hlen - nlen + 1 and haystack[ph] != needle[0]:
                ph += 1
            
            pn = curr = 0
            # ph指针所指位置等于needle的首字母时，pn指针于ph指针开始工作
            while pn < nlen and ph < hlen and haystack[ph] == needle[pn]:
                pn += 1
                ph += 1
                curr += 1
            
            # curr 等于 nlen时，说明找到字符串，返回结果即可，否则继续向后查找
            if curr == nlen:
                return ph - nlen
            
            ph = ph - curr + 1
        return -1
                

# @lc code=end
