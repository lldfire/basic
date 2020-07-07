#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#


# @lc code=start
# 双指针
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            # 判断不是字母或数字,索引+1
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    print(s[left], s[right])
                    return False
                left += 1
                right -= 1
            # else:
            #     return False
            # print(s[left], s[right])d
        return True


print(Solution().isPalindrome("."))
# @lc code=end

