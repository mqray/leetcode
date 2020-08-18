# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/13 7:27 PM

class Solution:
    def IsValidExp(self , s ):
        # write code here
        # 判断是否匹配的括号
        if not s: return True
        hashmap = {')':'(',']':'[','}':'{'}
        stack = []
        for ch in s:
            #入栈的时候如果栈是空，且入栈的是右括号，直接出
            # 如果是左括号，入栈，
            # 碰到右括号，判断是否与栈顶元素匹配
            if ch not in hashmap: #左括号入栈
                stack.append(ch)
            else:
                if not stack: return False#如果当前元素是右括号，且栈空，False
                # top_ele = hashmap.get(ch,'#')#如果有的话
                if hashmap.get(ch) != stack[-1]:
                    return False
                else:
                    stack.pop()
        return True
s = Solution()
res = s.IsValidExp('{()}}}')
print(res)
