# 时间复杂度：O（NlogK）.N是strs长度，K为单词最大长度
# 空间复杂度：O（NK）.所有单词都存储了
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1.结果字典dict
        result = {}
        # 2。遍历每个单词
        for str in strs:
            # 3。排序
            sort_str = ''.join(sorted(list(str)))
            # 4。字典表统计分类
            if not sort_str in result:
                result[sort_str] = []
            result[sort_str].append(str)
        #    5。返回结果
        return list(result.values())
