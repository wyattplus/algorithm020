# 时间复杂度：O（mn）
# 空间复杂度：O（mn）
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 基础判断
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        max_value = 0
        # 设定初始化的二维数组
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        # dp嵌套循环
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        # dp状态转移方程
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    #     局部最优解
                    max_value = max(max_value, dp[i][j])

        max_area = max_value * max_value
        return max_area
