# 时间复杂度：O（1）
# 空间复杂度：O（1）
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return (n & (n - 1)) == 0
