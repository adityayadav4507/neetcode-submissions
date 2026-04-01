# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        roott=root
        if p.val< roott.val and q.val <roott.val:
            return self.lowestCommonAncestor(roott.left,p,q)
        if p.val> roott.val and q.val >roott.val:
            return self.lowestCommonAncestor(roott.right,p,q)
        else: 
            return roott