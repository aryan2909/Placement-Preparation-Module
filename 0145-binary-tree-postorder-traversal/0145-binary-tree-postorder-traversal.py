from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.postorder(root, result)
        return result
    
    def postorder(self, node: Optional[TreeNode], result: List[int]) -> None:
        if node is None:
            return
        
        self.postorder(node.left, result)
        self.postorder(node.right, result)
        result.append(node.val)
