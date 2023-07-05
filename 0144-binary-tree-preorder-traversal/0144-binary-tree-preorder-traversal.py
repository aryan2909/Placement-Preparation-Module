from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.preorder(root, result)
        return result
    
    def preorder(self, node: Optional[TreeNode], result: List[int]) -> None:
        if node is None:
            return
        
        result.append(node.val)
        self.preorder(node.left, result)
        self.preorder(node.right, result)
