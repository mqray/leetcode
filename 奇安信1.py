# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/16 3:17 PM

#
# @param num_money int整型 奖金的总数,单位为元
# @return int整型
#
class Solution:
    def CalulateMethodCount(self, num_money):
        # write code here
        # 求公比为2的等比数列 死活就是不过 md
        if num_money == 0: return 0
        return 2**(num_money-1)
s = Solution()
res = s.CalulateMethodCount(3)
print(res)
