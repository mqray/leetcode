# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/14 4:39 PM

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1.暴力法
        # 2.hashmap
        hashmap = {}
        # for i, num in enumerate(nums):
        #     hashmap[num] = i
        # for i, num in enumerate(nums):
        #     other = hashmap.get(target-num)#直接去找target-num，找到就return
        #     if other and i!=other:#避免是同一个数
        #         return [i,other]
        for i, num in enumerate(nums):
            other = hashmap.get(target - num)#先查target-num在不在hashmap中
            if other is not None:
                return [other, i]
            hashmap[num] = i
s = Solution()
res = s.twoSum([1,3,4,2],6)
print(res)