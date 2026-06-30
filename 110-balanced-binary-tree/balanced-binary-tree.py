class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            left_height = check_height(node.left)
            if left_height == -1: 
                return -1
                
            right_height = check_height(node.right)
            if right_height == -1: 
                return -1
            
            # If the current node is unbalanced, bubble up -1
            if abs(left_height - right_height) > 1:
                return -1
                
            # Otherwise, return the actual height of this subtree
            return 1 + max(left_height, right_height)
        
        return check_height(root) != -1