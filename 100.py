# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def dfs(re, tree):
            if(tree == None):
                re.append('null')
                return
            else:
                re.append(tree.val)
                dfs(re, tree.left)
                dfs(re, tree.right)

        re1 = []
        re2 = []

        dfs(re1, p)
        dfs(re2, q)

        if(re1 == re2):
            return True
        else:
            return False

作者：s2-
链接：https://leetcode-cn.com/problems/same-tree/solution/xiao-bai-bu-yi-by-s2-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。