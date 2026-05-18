# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        res = []

        def inorder(root):
            
            if root is None:
                return 

            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        
        l = 0
        r = 1

        inorder(root)
        print(res)
        
        while r < len(res):
            if res[l] < res[r]:
                l += 1
                r += 1
            else:
                return False
        
        return True
