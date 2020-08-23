# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/21 8:08 PM

# 斐波拉切蛇
# 先弄出 n*n个斐波拉切数 放到对应的位置
# 1 1 2 3 5 8 13 21 34 55
import sys
n = int(sys.stdin.readline())
# 先求出斐波那契数组
size = n*n
nums = [1]
a,b = 1, 1
for i in range(2,size+1):
    a,b = b,b+a
    nums.append(a)
print(nums)
# nums = []
nums = [nums[i*n:(i+1)*n] for i in range(n-1,-1,-1)]
print(nums)
res = []
def printFib(start):
    col_end, row_end = n-start-1, n-start-1
    for col in range(start, col_end+1):
        res.append(nums[start][col])
    if start<row_end:
        for row in range(start+1,row_end+1):
            res.append(nums[row][col_end])
    if start<col_end and start>row_end:
        for col in range(col_end-1,start-1,-1):
            res.append(nums[row_end][col])
    if start<row_end and start<col_end:
        for row in range(row_end-1,start,-1):
            res.append(nums[row][start])
start = 0
# 只有n//2圈
while n > 2*start:
    printFib(start)
    start += 1
printFib(res)

