# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:    
        best = [0]
        best[0] = 0

        def dfs(node) -> int:
            if node == None:
                return -1
            
            leftDiameter = 1 + dfs(node.left)
            rightDiameter = 1 + dfs(node.right)

            total = leftDiameter + rightDiameter

            best[0] = max(best[0], total)

            return max(leftDiameter, rightDiameter)

        dfs(root)

        return best[0]
