# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
    
        def dfs(root, length):
            if(not root):
                return 0
            if(not root.left and not root.right):
                return length

            len1 = dfs(root.left, length + 1)
            len2 = dfs(root.right, length + 1)

            return min(len1, len2) if(len1 > 0 and len2 > 0)else len1 + len2

        return dfs(root, 1)
