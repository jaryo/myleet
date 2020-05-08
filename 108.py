# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        length = len(nums)

        def dfs(nums, l, r):
            if(l > r):
                return None
            
            mid = (l + r) / 2
            t = TreeNode(nums[mid])
            t.left = dfs(nums, l, mid-1)
            t.right = dfs(nums, mid+1, r)
            return t
        
        return dfs(nums, 0, length - 1)