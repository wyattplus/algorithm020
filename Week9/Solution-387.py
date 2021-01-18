# 时间复杂度：O(n)
# 空间复杂度：O(∣Σ∣)
import collections


# 队列思想处理问题
class Solution:
    def firstUniqChar(self, s: str) -> int:
        index = dict()
        queue = collections.deque()
        n = len(s)
        for i, char in enumerate(s):
            if char not in index:
                index[char] = i
                queue.append((s[i], i))
            else:
                index[char] = -1
                while queue and index[queue[0][0]] == -1:
                    queue.popleft()
        if not queue:
            return -1
        else:
            return queue[0][1]
