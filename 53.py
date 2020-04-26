class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        num = nums[0]
        maxNum = nums[0]
        temp = 0

        for i in range(length):
            temp += nums[i]
            num = max(nums[i], temp)
            temp = max(temp, num)
            if (num > maxNum):
                maxNum = num
        return maxNum