# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/14 8:45 PM

# 10.0.3.193
# 167969729
# 167773121
# 10.3.3.193
import sys
tmp = sys.stdin.readline()
nums = map(int, tmp.strip('\n').split('.'))
res = 0
for i, num in enumerate(nums):#[0,1,2,3]=24,16,8,0
    left = 24- (i*8)
    res += (num<<left)
print(res)
# 167969729
num = sys.stdin.readline()
strs = str(bin(int(num)))[2:].zfill(32)
# print(strs.zfill(32))
res = [strs[0:8],strs[8:16],strs[16:24],strs[24:]]

ips = []
x = 128
for i in range(4):
    ip=0
    x = 128
    left, right = 0, 7
    while left <= right:
        cur = int(res[i][left])
        ip += cur * x
        x = x >> 1
        left += 1
    ips.append(ip)
ips = list(map(str,ips))
print('.'.join(ips))

