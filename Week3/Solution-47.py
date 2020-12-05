# 时间复杂度：O（）
# 空间复杂度：O（）
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, level, stack, used, result):
            # terminator
            if level == len(nums):
                result.append(stack[:])
                return
            # process
            for i in range(len(nums)):
                # 使用过的，直接跳过
                if used[i]:
                    continue
                #     比不重复情况，多这一个判断。需要在排序后的与i-1比较
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                stack.append(nums[i])
                used[i] = True
                # drill down
                dfs(nums, level + 1, stack, used, result)
                # reverse state
                stack.pop()
                used[i] = False

        # init
        result, stack, used = [], [], [False] * len(nums)
        nums.sort()
        dfs(nums, 0, stack, used, result)
        return result
