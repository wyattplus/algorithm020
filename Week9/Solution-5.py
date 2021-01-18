# 时间复杂度：O(n^2)
# 空间复杂度：O(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        result = ""

        for l in range(n):

            for i in range(n):
                j = i + l
                if j >= len(s):
                    break
                #   下方dp方程
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(result):
                    result = s[i:j + 1]
        return result
