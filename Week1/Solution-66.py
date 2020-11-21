# 时间复杂度：O（n）
# 空间复杂度：O（1）
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 1.从后向前迭代数组
        for i in range(len(digits) - 1, -1, -1):
            # 2.自增1，取余。
            digits[i] += 1
            digits[i] %= 10
            # 3.如果存在余数非0，则代表该数组结束进位
            if digits[i] != 0:
                return digits
        # 4.当9999，类似情况时，直接加一位1即可。其他为填充0
        digits = [0 for _ in range(len(digits) + 1)]
        digits[0] = 1
        return digits
