# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        re = []

        def dfs(root):
            if(not root):
                return

            dfs(root.left)
            re.append(root.val)
            dfs(root.right)
        
        dfs(root)

        return re[k-1]