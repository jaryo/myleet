class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)

        for i in range(length):
            if(target > nums[i]):
                continue
            else:
                return i
        
        return length