# 时间复杂度：O（N）
# 空间复杂度：O（1）
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # 初始化five与ten数量
        five, ten = 0, 0
        # 贪心算法+迭代
        for bill in bills:
            # bill为5的情况
            if bill == 5:
                five += 1
            # bill为10的情况
            elif bill == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            # bill为20的情况
            else:
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
