# 时间复杂度：O（n）
# 空间复杂度：O（n）
from typing import List

from Week2.Node import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def helper(preorder, inorder, pre_left, pre_right, in_left, in_right) -> TreeNode:
            # terminator
            if pre_left > pre_right or in_left > in_right:
                return None
            # process
            root_value = preorder[pre_left]
            root = TreeNode(root_value)
            p_index = tree_dict.get(root_value)
            # drill down
            root.left = helper(preorder, inorder, pre_left + 1, p_index - in_left + pre_left, in_left, p_index - 1)
            root.right = helper(preorder, inorder, p_index - in_left + pre_left + 1, pre_right, p_index + 1,
                                in_right)
            return root

        if len(preorder) != len(inorder):
            return None;
        tree_dict = dict()
        for i in range(len(inorder)):
            tree_dict[inorder[i]] = i
        return helper(preorder, inorder, 0, len(preorder) - 1, 0, len(inorder) - 1)
