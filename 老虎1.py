# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/16 5:10 PM

# 打印 数组中和为k的二元组
import sys
size, target = map(int,sys.stdin.readline().split())
left, right = 0, size-1
nums = list(map(int,sys.stdin.readline().split()))
while left < right:
    cur = nums[left] + nums[right]
    if cur == target:
        while left<right and nums[left] == nums[left+1]:
            left += 1
        while left < right and nums[right] == nums[right-1]:
            right -= 1
        print(nums[left], nums[right])
        left, right = left + 1, right - 1
    elif cur < target:
        left += 1
    else:
        right -= 1

