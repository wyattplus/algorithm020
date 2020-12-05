# 时间复杂度：O(n * n!).其中 nn 为序列的长度
# 空间复杂度：O（n）
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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
                stack.append(nums[i])
                used[i] = True
                # drill down
                dfs(nums, level + 1, stack, used, result)
                # reverse state
                stack.pop()
                used[i] = False
        # init
        result, stack, used = [], [], [False] * len(nums)
        dfs(nums, 0, stack, used, result)
        return result
