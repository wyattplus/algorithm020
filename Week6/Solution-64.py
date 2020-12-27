# 时间复杂度：O（mn）
# 空间复杂度：O（mn）
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 基础判断
        if not grid or not grid[0]:
            return 0
        # 设定行列
        rows_count, columns_count = len(grid), len(grid[0])
        # 创建dp二维数组
        dp = [[0] * columns_count for _ in range(rows_count)]
        dp[0][0] = grid[0][0]
        # 遍历，填充每个格子最优解
        for i in range(1, rows_count):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, columns_count):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        # 2层遍历结果，取过程中最小值
        for i in range(1, rows_count):
            for j in range(1, columns_count):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[rows_count - 1][columns_count - 1]

