# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/15 4:46 PM


# 输出1-N中所有的逆序数对 逆序数对的含义是 假设原始a,b是逆序对 现在的定义是4a = b
# n 1e7
# 每行输出一个逆序对
import sys
def main():
    n = int(sys.stdin.readline())
    res = set()
    count = 0
    for i in range(10,n//2):
        rev = rever(i)
        if i in res or rev in res:
            continue
        if rev == 4*i or 4*rev == i:
            res.add((rev,i)) if rev*4 == i else res.add((i,rev))
            count += 1
    print(count)
    for cup in res:
        print(cup[0],cup[1])
def rever(num):#先求它的逆序数
    cur = str(num)
    a = int(cur[0])
    b = int(cur[-1])
    if 4*a !=b or 4*b!=a:
        return 0
    return int(cur[::-1])
    # return int(cur[::-1])
    # cur = list(str(num))
    # print(type(cur[1]))
    # left,right = 0,len(cur)-1
    # while left<right:
    #     cur[left],cur[right] = cur[right],cur[left]
    #     left,right = left+1, right -1
    # cur = ''.join(cur)
    # return int(cur)

main()





