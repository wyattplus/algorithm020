
from typing import List

from Week2.Node import TreeNode


class Solution:
    # 时间复杂度：O（N）
    # 空间复杂度：O（N）
    # 1。迭代法
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 1.初始化stack 和结果
        stack, result = [], []
        # 2。基础判断
        if root == None:
            return result
        # 3。遍历root 和 stack
        while root or stack:
            # 4。中序遍历特点，将left入栈
            while root:
                stack.append(root)
                root = root.left
            # 5。取出stack，并进行右分支遍历
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result
