# 时间复杂度：O（n）
# 空间复杂度：O（k）,k=26
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1.判断长度是否一致
        if len(s) != len(t):
            return False
        # 2.初始化结果数组
        result = [0] * 26
        # 3.遍历，如果差值进行正负赋值
        for i in range(len(s)):
            result[ord(s[i]) - ord("a")] += 1
            result[ord(t[i]) - ord("a")] -= 1
        # 4。判断最后结果
        for i in range(26):
            if result[i] != 0:
                return False
        return True
