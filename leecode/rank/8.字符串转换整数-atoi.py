#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#


# @lc code=start
# class Solution:
#     """ 最基本的顺序判断,十分臃肿 """
#     def myAtoi(self, str: str) -> int:
#         int_max = 2 ** 31 - 1
#         int_min = -2 ** 31
#         str = str.lstrip()
#         res = 0
#         flag = 1
#         for i, c in enumerate(str, 0):
#             # print(res)
#             if i == 0:
#                 if c == '+':
#                     if c == str:
#                         return 0
#                     pass
#                 elif c == '-':
#                     if c == str:
#                         return 0
#                     flag = -1
#                 elif c.isdigit():
#                     res = res * 10 + int(c)
#                     # print(res)
#                     if c == str:
#                         return res
#                 else:
#                     return 0

#             if i > 0:
#                 if c.isdigit():
#                     res = res * 10 + int(c)
#                 else:
#                     return min(int_max, res) if flag > 0 else max(int_min, -1 * res)
#         return min(int_max, res) if flag > 0 else max(int_min, -1 * res)
INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31


class AutoMaton:
    def __init__(self):
        super().__init__()
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        # 类似于状态转移的方式
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end']
        }

    def get_col(self, c):
        """ 根据字母类型改变当前状态 """
        if c.isspace():
            return 0
        elif c == '-' or c == '+':
            return 1
        elif c.isdigit():
            return 2
        else:
            return 3

    def get(self, c):
        # 根据该字母类型修改当前状态
        # print(self.state)
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(
                self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == "+" else -1


class Solution:
    """ 使用官方的自动机算法 """
    def myAtoi(self, str: str) -> int:
        auto = AutoMaton()
        for c in str:
            auto.get(c)
            if auto.state == 'end':
                break
        return auto.ans * auto.sign


print(Solution().myAtoi('+1123423412323ddsa asda'))
# @lc code=end

