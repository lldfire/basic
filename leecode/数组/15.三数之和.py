#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
from typing import List


# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        res = []
        for n in range(len(nums)):
            if nums[n] > 0:
                return res
            # 避免同一个查找值，多次查找
            if n > 0 and nums[n] == nums[n - 1]:
                continue
            l = n + 1
            r = len(nums) - 1

            while l < r:
                # 计算结果等于0，同时移动两个指针，去查找下一个可能结果
                if nums[n] + nums[l] + nums[r] == 0:
                    res.append([nums[n], nums[l], nums[r]])
                    # 避免两个指针上的数字相同，导致重复就算
                    while (l < r) and (nums[l] == nums[l + 1]):
                        l += 1
                    while (l < r) and (nums[r] == nums[r - 1]):
                        r -= 1
                    l += 1
                    r -= 1
                # 计算结果大于0，右指针左移，减小计算结果
                elif nums[n] + nums[l] + nums[r] > 0:
                    r -= 1
                # 计算结果小于0，左指针右移，增大计算结果
                else:
                    l += 1
        return res


nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))

# @lc code=end

