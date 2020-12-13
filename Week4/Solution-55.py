# 时间复杂度：O（N）
# 空间复杂度：O（1）
from typing import List


# 贪心算法
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 特殊情况
        if nums is None:
            return False

        index = len(nums) - 1
        # 从后向前推倒，进行迭代
        for i in range(len(nums) - 1, -1, -1):
            # 如果当前的可走步数大于俩格子间的距离，就可以选择该格子
            if nums[i] >= index - i:
                index = i
        return index == 0
