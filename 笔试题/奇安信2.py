# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/16 3:40 PM

# hello undo redo world. hello undo redo world.
import sys
strs = sys.stdin.readline().split()
# print(strs)
stack = []
left, right = 0, len(strs)-1
tmp = ''
# 遇到redo恢复之前的撤销掉的字符串
# 先假设所有的undo、redo在一起
while left <= right:
    ch = strs[left]
    if ch != 'redo' and ch != 'undo':
        stack.append(ch)
    elif ch == 'undo':
        if stack:#如果stack中有东西
            tmp = stack.pop()
    elif ch == 'redo':
        if tmp!='':
            stack.append(tmp)
    left += 1
print(' '.join(stack))
# while left <= right:
#     ch = strs[left]
#     if not stack:#如果为空
#         if ch == 'redo' or ch =='undo':
#
#         if ch != 'undo' or ch != 'redo':
#             stack.append(ch)
#         if ch == 'redo':
#             if tmp != '':
#                 stack.append(tmp)
#         left += 1
#     else:
#         if ch == 'undo':
#             if left+1 <= right and strs[left+1] != 'redo':
#                 stack.pop()
#                 left += 1
#             elif left+1 <= right and strs[left+1] == 'redo':
#                 left += 2
#         elif ch == 'redo':
#             if tmp != '':
#                 stack.append(tmp)
#                 tmp = ''
#                 left += 1
#         else:
#             stack.append(ch)
#             left+=1
# print(' '.join(stack))
