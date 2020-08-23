# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/23 4:09 PM

# ESSWNEE n向上 s向下 w向西 e向东
# 判断是否走到过之前的位置
# 即判断向上、向左走 是否等于向下 向右走


# def isCross(strs):
#     c1,c2,c3,c4 = 0,0,0,0#
#     for ch in strs:
#         if ch == 'N':
#             c1 += 1
#         elif ch == 'S':
#             c2 -= 1
#         elif ch == 'E':
#             c3 += 1
#         elif ch == 'W':
#             c4 -= 1
#         if c1 == c2 and c3 == c4:
#             print('True')
#             return True
#     print('False')
#     return False
def isCross(strs):
    i, j = 0, 0
    tmp = []
    for ch in strs:
        if ch == 'N':
            i += 1
        elif ch == 'S':
            i -= 1
        elif ch == 'E':
            j += 1
        elif ch == 'W':
            j -= 1
        if [i, j] in tmp:
            print('True')
            return True
        else:
            tmp.append([i,j])
    print('False')
    return False
import sys
strs = sys.stdin.readline()
isCross(strs)