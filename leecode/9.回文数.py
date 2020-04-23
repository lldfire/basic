#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    """"""
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        right = 0

        while x > right:
            print(x, right)
            right = right * 10 + x % 10
            x //= 10
        print(x, right)
        return x == right or x == right // 10


print(Solution().isPalindrome(0))
# @lc code=end

