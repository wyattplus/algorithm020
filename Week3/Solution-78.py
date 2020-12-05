# 时间复杂度：O（）
# 空间复杂度：O（）
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            print(i)
            res += [[i] + num for num in res]
        return res
