# 时间复杂度：O（n）
# 空间复杂度：O（1）
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        # 初始前面f（0）f（1）f（2）
        a, b, c = 0, 1, 2
        # 迭代出结果
        for i in range(n - 2):
            a, b = b, c
            c = a + b
        return c
