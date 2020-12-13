# 时间复杂度：O（logn）
# 空间复杂度：O（1）
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            # 求中位
            mid = (left + right) >> 1
            # 多重条件，注重此题的核心就在此
            if nums[mid] >= nums[0] and (target > nums[mid] or target < nums[0]):
                left = mid + 1
            elif nums[mid] < target < nums[0]:
                left = mid + 1
            else:
                right = mid
        #  if else 简化代码
        return left if left == right and nums[left] == target else -1
