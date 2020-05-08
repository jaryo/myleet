# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if(not root):
            return []

        re = []
        num = 0

        def query(root, num):
            re.append([])
            
            if(root):
                re[num].append(root.val)
            
            if(root.left):
                query(root.left, num+1)
            if(root.right):
                query(root.right, num+1)

        query(root, num)

        while([] in re):
            re.remove([])

        return re[::-1]
