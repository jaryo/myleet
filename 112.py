# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if(not root):
            return False

        def dfs(root, num):
            if(not root):
                return False
            if(not root.left and not root.right):
                return num - root.val == 0

            return dfs(root.left, num - root.val) or dfs(root.right, num - root.val)
        
        return dfs(root, sum)