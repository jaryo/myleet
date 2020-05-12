# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if(not root):
            return True

        def dfs(root, length):
            if(not root):
                return length - 1
            
            len1 = dfs(root.left, length + 1)
            len2 = dfs(root.right, length + 1)

            if(abs(len1 - len2) > 1):
                return -2
            
            return max(len1, len2)
            
        return (False if(dfs(root, 0) == -2)else True)