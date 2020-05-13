# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if(not root):
            return []

        re = []

        def bfs(root):
            queue= []
            num = 0
            queue.append(root)
            while(queue):
                temp = []
                length = len(queue)
                for i in range(length):
                    node = queue.pop(0)
                    if(num % 2 == 0):
                        temp.append(node.val)
                    else:
                        temp.insert(0, node.val)
                    if(node.left):
                        queue.append(node.left)
                    if(node.right):
                        queue.append(node.right)
                re.append(temp)
                num += 1
        
        bfs(root)

        return re
