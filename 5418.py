# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.re = 0
        count = [0 for x in range(10)]
        temp = []
        def dfs(root):
            temp.append(root.val)
            if(not root.left and not root.right):
                for i in temp:
                    count[i] += 1
                pos = 0
                for i in count:
                    if(i % 2 != 0 and i > 0):
                        pos += 1
                if(pos <= 1):
                    self.re += 1
                for i in range(10):
                    count[i] = 0
            
            if(root.left):
                dfs(root.left)
            if(root.right):
                dfs(root.right)
            temp.pop()
        
        dfs(root)  
        return self.re