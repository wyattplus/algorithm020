# 时间复杂度：O（n）
# 空间复杂度：O（n）
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1.字典表，key为值，value为下标
        table = dict()
        for i, num in enumerate(nums):
            # 2.一个减法得到期望值
            expectedValue = target - num
            # 3.对期望值进行hash表查询
            if expectedValue in table:
                # 4.返回下标数组，并且table[expectedValue]< i.保证了下标顺序
                return [table[expectedValue], i]
            # 5.插入字典hash对
            table[nums[i]] = i
        return []
