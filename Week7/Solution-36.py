# 时间复杂度：O（1）
# 空间复杂度：O（1）
class Solution:
    def isValidSudoku(self, board):
        # 初始化row columns blocks
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        blocks = [{} for i in range(9)]

        # 遍历数独
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    # 可以使用 block_index = (row / 3) * 3 + columns / 3
                    block_index = (i // 3) * 3 + j // 3

                    # row column block进行保存，方便后续进行重复判定
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    blocks[block_index][num] = blocks[block_index].get(num, 0) + 1

                    # 进行重复判断，如果已存在则false
                    if rows[i][num] > 1 or columns[j][num] > 1 or blocks[block_index][num] > 1:
                        return False
        return True
