# 时间复杂度：O(N!)
# 空间复杂度：O(N)
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 生成棋盘
        def generate():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        # 回溯遍历
        def backTrack(row: int):
            # 最后一行生程棋盘
            if row == n:
                board = generate()
                result.append(board)
            else:
                # 判断是否在行，撇，捺里面
                for i in range(n):
                    if i in columns or row - i in pie or row + i in na:
                        continue
                    #     process
                    queens[row] = i
                    columns.add(i)
                    pie.add(row - i)
                    na.add(row + i)
                    # drill down
                    backTrack(row + 1)
                    # reserve state
                    columns.remove(i)
                    pie.remove(row - i)
                    na.remove(row + i)

        result = list()
        queens = [-1] * n
        columns = set()
        pie = set()
        na = set()
        row = ["."] * n
        backTrack(0)
        return result
