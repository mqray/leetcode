# # -*- coding:utf-8 -*-
# # Author : Ray
# # Data : 2020/8/22 7:37 PM
#
# # 圆柱体最大子矩阵的和
# # dp[i][j]表示到该处的最大矩阵和
# import sys
# m,n = map(int,sys.stdin.readline().strip().split())
# # m是行 n是列
# nums = []
# for i in range(m):
#     cur = map(int,sys.stdin.readline().split())
#     nums.append(list(cur))
# dp = [[0]*(n) for _ in range(m)]
# for i in range(m):
#     dp[i][0] = max(dp[i-1][0] + nums[i][0], dp[i-1][0])
# for j in range(n):
#     dp[0][j] = max(dp[0][j-1] + nums[0][j], dp[0][j-1])
# for i in range(1,m):
#     for j in range(1,n):
#         # if nums[i][j] >= 0:
#         dp[i][j] = max(dp[i-1][j],dp[i][j-1],dp[i][j-1] + dp[i-1][j] + nums[i][j] - dp[i-1][j-1])
# print(dp)
# print(dp[-1][-1])
# '''
# 3 3
# 2 -1 2
# 3 0 4
# 1 7 0
# '''
#
#
import sys
m,n = map(int,sys.stdin.readline().strip().split())
if n>15:
    print(0)
count = 0
while m>2:
    m = m>>1
    count += 1
# print(count-n)