# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(not root):
            return 0
            
        def getdepth(r):
            num = 0
            while(r):
                num += 1
                r = r.left

            return num
        
        ld = getdepth(root.left)
        rd = getdepth(root.right)

        if(ld == rd):
            return 2**ld + self.countNodes(root.right)
        else:
            return 2**rd + self.countNodes(root.left)
