from typing import List


# 时间复杂度：O（n）.n个元素反转3次
# 空间复杂度：O（1）
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1.取余，以防越界
        k %= len(nums)
        # 2.整个数组反转
        self.reverse(nums, 0, len(nums) - 1)
        # 3.前k个元素再次反转
        self.reverse(nums, 0, k - 1)
        # 4.后面 len(nums) - k个元素反转，即为结果
        self.reverse(nums, k, len(nums) - 1)

    # 反转函数
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
