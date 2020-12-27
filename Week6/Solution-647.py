# 时间复杂度：O（n2）
# 空间复杂度：O（1）
class Solution:
    def countSubstrings(self, s: str) -> int:
        # 基础判断
        if s is None or s == "":
            return 0
        n, result = len(s), len(s)
        # 生成初始化dp二维数组
        dp = [[False for i in range(n)] for j in range(n)]

        for i in range(n):
            dp[i][i] = True
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if j - i == 1:
                        # i和j相邻情况为true
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False
                if dp[i][j]:
                    result += 1
        return result
