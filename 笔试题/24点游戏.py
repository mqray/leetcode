# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/22 3:11 PM
from typing import List
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0]-24) < 1e-6
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        candidates = [nums[k] for k in range(len(nums)) if k!=i and k!=j]
                        if dfs(candidates+[nums[i] + nums[j]]):
                            return True
                        if dfs(candidates+[nums[i] - nums[j]]):
                            return True
                        if dfs(candidates+[nums[i] * nums[j]]):
                            return True
                        if nums[j] != 0 and dfs(candidates + [nums[i]/nums[j]]):
                            return True
            return False
        if not nums: return False
        return dfs(nums)

s = Solution()
res = s.judgePoint24([1,2,3,4])
print(res)