# 时间复杂度：O（n）
# 空间复杂度：O（1）
from typing import List


class Solution:
    # 方法1：双指针交换
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        # 1.设定慢指针，此指针代表下一个需要赋值的下标
        slowIndex = 0
        for i in range(len(nums)):
            # 2.值不为0时，需要将slowIndex赋值，并且后移一位
            if nums[i] != 0:
                # 3.python交换俩值，很方便
                nums[slowIndex], nums[i] = nums[i], nums[slowIndex]
                slowIndex += 1

    # 方法2：关注每个非零数组前面存在几个"0"
    def moveZeroes(self, nums: List[int]) -> None:
        # 1.统计当前已经有几个"0"
        zeroCount = 0
        for i in range(len(nums)):
            # 2.当前值为0时，count+1
            if nums[i] == 0:
                zeroCount += 1
            else:
                # 3.精髓所在，将nums[i - zeroCount]的位置，赋值
                nums[i - zeroCount] = nums[i]
        # 4.对于数字都前移后，最后zeroCount数量的位置直接赋值0
        nums[len(nums) - zeroCount:len(nums)] = [0 for _ in range(zeroCount)]
