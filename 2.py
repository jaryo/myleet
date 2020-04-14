class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            target1 = target - nums[i]
            for j in range(i+1, len(nums)):
                if(target1 == nums[j]):
                    return [i,j]