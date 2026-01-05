# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = []
        def dfs(node, maxSoFar):
            if node is None:
                return
            
            if node.val >= maxSoFar:
                good.append(node.val)
                maxSoFar = node.val

            dfs(node.left, maxSoFar)
            dfs(node.right, maxSoFar)
        dfs(root, root.val)   
        
        return len(good)