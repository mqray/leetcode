# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/23 3:57 PM

# 是否有效括号

def isValid(strs):
    hashmap = {')':'(',']':'[','}':'{'}
    stack = []
    # ()}[]
    # ()()()
    for ch in strs:
        if ch not in hashmap:
            stack.append(ch)
        else:
            top_ele = hashmap.get(ch)
            if not stack:
                print('False')
                return False
            else:
                if top_ele != stack[-1]:
                    print('False')
                    return False
                else:
                    stack.pop()
    print('True')
    return stack == []
import sys
strs = sys.stdin.readline()
isValid(strs)




