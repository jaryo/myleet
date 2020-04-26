# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if(root == None):
            return True
        elif(root.left == None and root.right == None):
            return True

        def judge(le, ri):
            if(not le and not ri):
                return True
            elif(not le or not ri):
                return False
            if(le.val == ri.val):
                re1 = judge(le.left, ri.right)
                re2 = judge(le.right, ri.left)
                return re1 and re2
            else:
                return False
        
        return judge(root.left, root.right)