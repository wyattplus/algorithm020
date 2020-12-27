# 时间复杂度：O（n）
# 空间复杂度：O（1）
class Solution:
    def numDecodings(self, s: str) -> int:
        # 基础判断
        if len(s) == 0:
            return 0
        # 设置dp起点
        dp = [1, 0]
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(1, len(s)):
            dp.append(0)
            if s[i] != '0':
                dp[-1] += dp[-2]
            if '10' <= s[i - 1:i + 1] <= '26':
                dp[-1] += dp[-3]
            dp.pop(0)

        return dp[-1]


