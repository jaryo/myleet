class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = 0

        for i in range(len(nums) - 1):
            if(nums[i] == nums[i+1]):
                nums[i] = 0
                num = num + 1
        
        nums.sort()

        for i in range(num):
                nums.remove(0)
            
        return len(nums)