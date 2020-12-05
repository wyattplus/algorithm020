# 时间复杂度：O（？）有点难评估
# 空间复杂度：O（n）
from typing import List


# 递归，回溯思路。dfs方法
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(n, k, start, stack, result):
            # terminator
            if k == 0:
                result.append(stack[:])
                return
            # process
            for i in range(start, n - k + 1):
                stack.append(i)
                # drill down
                dfs(n, k - 1, i + 1, stack, result)
                # reverse state
                stack.pop()

        result, stack = [], []
        dfs(n, k, 1, stack, result)
        return result
