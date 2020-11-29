# 时间复杂度：O（N）
# 空间复杂度：O（N）
import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1.初始化值
        ans, result = [], [[] for i in range(len(nums) + 1)]
        # 2。字典统计
        result_dict = collections.Counter(nums)
        # 3。遍历字典
        for num, count in result_dict.items():
            result[count].append(num)
        # 4。降序统计
        for i in range(len(nums), 0, -1):
            if len(result[i]) == 0:
                continue
            ans.extend(result[i])
            if len(ans) == k:
                return ans
