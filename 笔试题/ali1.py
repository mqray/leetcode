# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/14 7:12 PM

import sys

'''
2 2
2 4
8 16
'''

def helper():
#     # 没必要 全部累计之后在判断，可以每次判断第一行到最大值要多少步，
#     # 每一行计算完毕之后，记住最大值，下一行依次扩展
#     # 最后根据全局最大值扩展，能扩展则累加数 不能则，返回-1
#     #
    max_val = float('-inf')
    nums = []
    m, d = map(int, input().split())
    for i in range(m):
        tmp = list(map(int,sys.stdin.readline().split()))
        nums.append(tmp)
        # cur = max(tmp)
        max_val = max(max_val,max(tmp))
    return nums,max_val,d

def main():
    nums, max_val,d = helper()
    print(nums,max_val,d)
    count = 0
    for i in range(len(nums)):
        for num in nums[i]:
            if (max_val - num) % d != 0:  # 16 1 2
                return -1
            else:
                count += (max_val - num) // d
    print(count)
    return count
main()

# def main():
#     m, d = map(int, input().split())
#     max_nums = []
#     count = 0
#     for i in range(m):
#         tmp = list(map(int,sys.stdin.readline().split()))
#         cur = max(tmp)
#         max_nums
#         for num in tmp:
#             if (cur-num)%d!=0:
#                 return -1
#             else:
#                 count += (cur-num)//d
#     for



