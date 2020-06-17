#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
from typing import List


# @lc code=start
# 理解：盛水最多，即面积最大，面积由两数较小者和两数之间的距离决定
# 较小数min(x1, x2),两数距离 abs(x1_idx - x2_idx)
# 方法一：双指针，移动较小数指针，因为较小指针不能再做容器的边界了
# 证明：
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l != r:
            temp = min(height[l], height[r]) * (r - l)
            ans = max(ans, temp)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans


he = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution().maxArea(he))

# @lc code=end
