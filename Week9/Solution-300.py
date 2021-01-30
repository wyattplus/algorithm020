# 时间复杂度：O(n^2)
# 空间复杂度：O（n）
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    # dp方程
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


class Solution(object):

    def myAtoi(self, s):
        if len(s) == 0: return 0
        ls = list(s.strip())
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-', '+']: del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit():
            ret = ret * 10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2 ** 31, min(sign * ret, 2 ** 31 - 1))
