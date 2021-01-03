from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = list()
        # 回溯法
        def generate(left_remain, right_remain, n, s):
            if left_remain == 0 and right_remain == 0:
                result.append(s)
            if left_remain != 0:
                generate(left_remain - 1, right_remain, n, s + "(")
            if right_remain != 0 and right_remain > left_remain:
                generate(left_remain, right_remain - 1, n, s + ")")

        generate(n, n, n, "")
        return result
