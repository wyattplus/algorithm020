# 时间复杂度：O（nlogn+mlogm）
# 空间复杂度：O（1）
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i, j = 0, 0
        # 排序
        g.sort()
        s.sort()
        # 田忌赛马的方式，继续从小最大贪心算法，每个孩子最优解
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
            j += 1
        return i
