# 时间复杂度：O（N）
# 空间复杂度：O（N）
class Solution(object):
    def reverseOnlyLetters(self, S: str) -> str:
        result = []
        l = len(result) - 1
        for i, x in enumerate(S):

            if x.isalpha():
                while not S[l].isalpha():
                    l -= 1
                result.append(S[l])
                l -= 1
            else:
                result.append(x)

        return "".join(result)
