# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/16 5:32 PM
#
# 返回两次操作后，数组元素之和的最小值
# @param nums int整型一维数组 这你你需要操作的数组
# @return long长整型
# 有点类似于找到柱状图的最大矩形面积
class Solution:
    def minimumValueAfterDispel(self , nums ):
        # write code here
        nums.sort()
        size1 = len(nums)
        max_area = 0
        ind1 = 0
        for i in range(size1):
            area = nums[i]*(size1-i)
            if area > max_area:
                max_area = area
                ind1 = i#记录下标
        delta1 = nums[ind1]
        tmp1 = []
        for num in nums:
            if num >= delta1:
                tmp1.append(num-delta1)
            else:
                tmp1.append(num)
        size2 = len(tmp1)
        tmp1.remove(0)
        ind2 = 0
        max_area2 = float('-inf')
        for i in range(size2):
            area = nums[i]*(size2-i)
            if area > max_area2:
                max_area2 = area
                ind2 = i
        delta2 = nums[ind2]
        tmp2 = []
        for num in nums:
            if num >= delta2:
                tmp2.append(num-delta2)
            else:
                tmp2.append(num)
        return sum(tmp2)

s = Solution()
res = s.minimumValueAfterDispel([1,2,3])
print(res)
