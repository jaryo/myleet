# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if(not root):
            return []

        re = []

        def bfs(root):
            queue = []
            queue.append(root)

            while(queue):
                length = len(queue)
                temp = []
                for i in range(length):
                    node = queue.pop(0)
                    temp.append(node.val)
                    if(node.left):
                        queue.append(node.left)
                    if(node.right):
                        queue.append(node.right)
                re.append(temp)
        
        bfs(root)
        
        return re