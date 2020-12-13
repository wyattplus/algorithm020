# 时间复杂度：O（n）
# 空间复杂度：O（1）
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        # 从index =1 开始
        for i in range(1, len(prices)):
            # 每步最优解
            if prices[i] > prices[i - 1]:
                result += prices[i] - prices[i - 1]
        return result
