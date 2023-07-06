from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.inorder(root, result)
        return result
    
    def inorder(self, node: Optional[TreeNode], result: List[int]) -> None:
        if node is None:
            return
        
        self.inorder(node.left, result)
        result.append(node.val)
        self.inorder(node.right, result)
