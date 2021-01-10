# 时间复杂度：O（mlogm+n）
# 空间复杂度：O（logm+n）
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def helper(x: int) -> (int, int):
            return rank[x] if x in rank else x

        n = len(arr2)
        rank = {x: i - n for i, x in enumerate(arr2)}
        arr1.sort(key=helper)
        return arr1
