#
# @lc app=leetcode.cn id=7 lang=python
#
# [7] 整数反转  −231,  231 − 1
#

# @lc code=start
# 速度慢，耗内存
# class Solution(object):
#     """ 改写为字符串，再通过字符串反转"""
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         maxx = 2 ** 31 - 1
#         minx = -2 ** 31
#         strx = str(x)
#         new_x = -int(strx[1:][::-1]) if '-' in strx else int(strx[::-1])
#         if new_x > maxx or new_x < minx:
#             return 0
#         else:
#             return new_x


class Solution(object):
    """ 官方解法，取余的方式推出最后一位数字，并判断是否溢出 """

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max_int = 2 ** 31 - 1
        min_int = -2 ** 31
        rev = 0
        while x != 0:
            pop = -(abs(x) % 10) if x < 0 else x % 10
            x = int(x / 10)
            if rev > int(max_int / 10) or (
                    rev == int(max_int / 10) and pop > 7):
                return 0
            if rev < int(min_int / 10) or (
                    rev == int(min_int / 10) and pop < -8):
                return 0
            rev = rev * 10 + pop
        return rev

        
# @lc code=end

print(Solution().reverse(-123))
