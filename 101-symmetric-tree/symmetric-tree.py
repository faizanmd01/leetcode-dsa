class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            # If both subtrees are empty, they are symmetric
            if not t1 and not t2: 
                return True
            # If only one is empty, or their values don't match, they aren't symmetric
            if not t1 or not t2 or t1.val != t2.val: 
                return False
            
            # Check if outer children and inner children are mirrors
            return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
        
        return isMirror(root, root)