# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/13 7:29 PM


class Solution:
    def GetCoinCount(self , N ):
        # write code here
        # 等价于拼凑出1024-N最少要花多少枚硬币
        if N == 1024: return 0
        coins = [1,4,16,64]
        dp = [float('inf')]*(1024-N+1)
        dp[0] = 0
        for i in range(1024-N+1):
            for coin in coins:
                if i>=coin:
                    dp[i] = min(dp[i],dp[i-coin]+1)
        return dp[-1]
s = Solution()
res = s.GetCoinCount(200)
print(res)


