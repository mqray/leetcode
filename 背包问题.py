# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/12 9:21 PM

# 1.背包容量N，物品m件，价值为V，每件物品只能取一次
# 最后返回的结果是至多装满N，得到的最大价值
class Solution:
    def backpack(self,N,weights,values):
        dp = [0]*(N+1)
        #千万注意for循环位置，以及遍历i时的正向与逆向
        for j in range(len(weights)):
            for i in range(N, -1, -1):
                if i >= weights[j]:#容量大于此物重量时
                    dp[i] = max(dp[i],dp[i-weights[j]]+values[j])
        return max(dp)
# s = Solution()
# weights = [2,2,6,5,4]
# values = [6,3,5,4,6]
#
# res = s.backpack(10,weights,values)
# print(res)

# 1.1 那如果问你，要恰好装满，能获得最大价值怎么办？
# 简单的做法是，将dp[1:]设置为正无穷
class SolutionI:
    def backpack(self,N,weights,values):
        # dp = [0]*(N+1)
        dp = [0] +[float('-inf')]*N#由于我们要求最大价值，这里就设置为-oo
        for j in range(len(weights)):
            for i in range(N, -1, -1):
                if i >= weights[j]:
                    dp[i] = max(dp[i],dp[i-weights[j]]+values[j])
        return max(dp)
# s = SolutionI()
# weights = [2,2,6,5,4]
# values = [6,3,5,4,6]
# res = s.backpack(10,weights,values)
# print(res)

# 2.背包容量N，物品m件，价值为V 每件物品可以取多次
class SolutionII:
    def backpack(self,N,weights,values):
        dp = [0]*(N+1)
        for j in range(len(weights)):
            for i in range(1, N):
                if i >= weights[j]:
                    dp[i] = max(dp[i],dp[i-weights[j]]+values[j])
        return max(dp)
s = SolutionII()
weights = [2,2,6,5,4]
values = [6,3,5,4,6]
res = s.backpack(10,weights,values)
print(res)