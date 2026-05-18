# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []

        if not root:
            return res
            
        queue = [root]

        while queue:
            
            curr_level = []

            for _ in range(len(queue)):
                
                curr_val = queue.pop(0)
                curr_level.append(curr_val.val)

                if curr_val.left:
                    queue.append(curr_val.left)
                
                if curr_val.right:
                    queue.append(curr_val.right)
                
            res.append(curr_level)
        
        return res