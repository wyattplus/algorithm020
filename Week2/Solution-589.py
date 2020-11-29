# 时间复杂度：O（）
# 空间复杂度：O（）
from typing import List

from Week2 import Node


class Solution:
    # 时间复杂度：O（N）
    # 空间复杂度：O（N）
    # 1。迭代
    def preorder(self, root: Node) -> List[int]:
        # 1。基础过滤
        if root is None:
            return []
        # 2。初始栈
        stack, result = [root], []
        # 3。遍历栈
        while stack:
            # 4。前序遍历，根左右
            n = stack.pop()
            result.append(n.val)
            # 调整顺序入栈
            stack.extend(n.children[::-1])
        return result

    # 时间复杂度：O（N）
    # 空间复杂度：O（N）
    # 2.递归
    def preorder2(self, root: Node) -> List[int]:
        def dfs(root):
            if root is None:
                return;
            result.append(root.val)
            if root.children is None:
                return
            for n in root.children:
                dfs(n)

        result = []
        dfs(root)
        return result
