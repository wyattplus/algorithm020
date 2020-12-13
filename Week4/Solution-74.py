# 时间复杂度：O（MN）
# 空间复杂度：O（1）
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_num = len(matrix)
        if row_num == 0:
            return False
        col_num = len(matrix[0])
        # 将二维矩阵调整为数组
        left, right = 0, row_num * col_num - 1

        while left <= right:
            # 二分查找找中间坐标
            mid_index = (left + right) >> 1
            # 找下标对应的数值
            mid_value = matrix[mid_index // col_num][mid_index % col_num]
            if target == mid_value:
                return True
            # 根据大小 进行左移或右移
            elif target < mid_value:
                right = mid_index - 1
            else:
                left = mid_index + 1
        return False
