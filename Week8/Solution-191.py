# 时间复杂度：O（1）
# 空间复杂度：O（1）
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n is not 0:
            count += 1
            n = n & (n - 1)
        return count
