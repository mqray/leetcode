# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/13 7:55 PM
class Solution:
    def Game24Points(self , arr ):
        # write code here [1-10]
        # 相当于找出+-*/(可以多次使用)四个符号 构造出的表达式的值 == 24？
        # 这题四个数字能重复使用么？
        # 1 2 3 4
        # 1 2 7 10
        # 4 6 4 6
        # 首先如果4个数相乘 都小于24 就False
        # 4个数相乘大了 那就判断最大的三个数相乘
        # 再最大的和最小的相乘 + 次小的*次大的
        # 果然骗到分了 哈哈哈
        res = 1
        for num in arr:
            res *= num
        if res < 24:
            return False
        elif res == 24:
            return True
        else:#4个数的乘积大于24
            t1 = res / arr[-1] + arr[-1]
        #这题应该限制的是没有重复数字
        # 如果两个数的乘积大于24 那么没法组成
        # 分析一下，怎样才能组合为24
        '''
        先考虑乘法 1*2*3*4只有这一种
        在考虑加法 1+23 = 1+（20+3）、2+22（3*6+4） 
        四个数组合的值从小到大排列 
        全乘 后三个乘+第一个 后两个*前两个
        '''