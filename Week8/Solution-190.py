# 时间复杂度：O（1）
# 空间复杂度：O（1）
class Solution:
    def reverseBits(self, n: int) -> int:
        result, a, b = 0, 0, 0
        for i in range(32):
            a = result << 1
            b = n & 1
            result = a + b
            n >>= 1
        return result
