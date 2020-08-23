# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/21 7:43 PM

# A+B = n
# A = abc
# B = acc
# n = 1068 a,b = 524 544
# a、b、c互不相同
# 二分求解 先对半拆
import sys
n = int(sys.stdin.readline())
# 如果n是奇数，没有 直接输出0
# 如果n是偶数 判断百位和个位是否相同 相同直接输出0
# 如果百位和个位不同，b从[0-9]除去百位、个位中选择
# 这个c不是固定的！
while True:
    if n&1:
        print(0)
        break
    x = n//2
    if x//100 == x % 10:
        res = 0 #要输出0
        print(0)
        break
    else:
        flag1 = x//100
        tmp = flag1*100
        tmp1 = [i for i in range(0,9)]
        cand1 = tmp1.remove(flag1)
        #先确定c 得到y的值
        ret, count = [], 0
        for c in cand1:
            y = tmp + 11*c
            target = n - y
            cand2 = tmp1.remove(c)

            for j in cand2:
                x = tmp + 10 * j + c
                if x == target:
                    ret.append((x,y))
                    count += 1


        flag2 = x%10
        # 534 -->544
        ret = []
        y = flag1*100 + flag2*10 + flag2
        target = n - y
        count = 0
        cadidates = [x for x in range(0,9) if x not in [flag2,flag1]]
        tmp = flag1*100 + flag2
        for i in cadidates:
            cur = tmp + 10*i
            if cur == target:
                ret.append(cur)
                count += 1
        print(count)
        for item in ret:
            print(item,y)
        break

