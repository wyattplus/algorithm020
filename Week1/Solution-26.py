from typing import List


# 时间复杂度：O（n）.遍历n个数
# 空间复杂度：O（1）
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 1.基础判断
        if len(nums) == 0:
            return 0
        # 2.设置慢指针，同时+1也是最终长度
        slowIndex = 0
        for fastIndex in range(len(nums)):
            # 3.有序数组，所以是递增。当快慢指针不同时，移动慢指针，同时赋值
            if nums[slowIndex] != nums[fastIndex]:
                slowIndex += 1
                nums[slowIndex] = nums[fastIndex]
        # 4.结果
        return slowIndex + 1
