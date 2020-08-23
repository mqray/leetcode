# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/23 3:16 PM

# N！后有多少个0
import sys
n = int(sys.stdin.readline())
# res = 1
# for i in range(2,n+1):
#     res *= i
# print(res)

# c2,c5,c10 = 0,0,0
# for i in range(n+1):
#     if i>=10 and i % 10 == 0:
#         c10 += 1
#     elif i>=5  and i % 5 == 0:
#         c5 += 1
#     elif i>=2 and i%2 == 0:
#         c2 += 0
# print(c2,c5,c10)
# res = c10 + min(c2,c5)
# print(res)
count = 0
for i in range(5,n+1,5):
    while i % 5==0:
        count +=1
        i = i//5
print(count)



