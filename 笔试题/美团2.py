# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/15 4:19 PM


import sys
def main():
    n = int(sys.stdin.readline())
    # 先将所有票放到list中
    if not n or n == 0: return 0
    tickets = []
    count = 0
    for i in range(n):
        cur = sys.stdin.readline().split()
        tickets += cur
    stack = [tickets[0]]
    left,right = 1,len(tickets)
    while left <= right-1:
        if not stack:
            stack.append(tickets[left])
            left += 1
        elif tickets[left] == stack[-1]:
            count += 1
            stack.pop()
            left += 1
        elif tickets[left] == tickets[left+1]:
            left += 2
    print(count)
    return count
main()

# beijing nanjing
# nanjing guangzhou
# guangzhou shanghai
# shanghai beijing
# fuzhou beijing
# beijing fuzhou
# beijing nanjing
# nanjing guangzhou
# guangzhou shanghai
# shanghai beijing
# fuzhou beijing
# beijing fuzhou
