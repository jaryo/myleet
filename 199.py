# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        re = []          
        def dfs(ele, size):
            if(ele):
                if(len(re) <= size):
                    re.append(ele.val)
                dfs(ele.right, size+1)
                dfs(ele.left, size+1)

        dfs(root, 0)
        return re