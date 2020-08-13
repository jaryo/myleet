class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if(not nums):
            return []

        re = []
        start = nums[0]
        end = nums[0]

        for i in range(1, len(nums)):
            if(nums[i] - 1 == nums[i-1]):
                end = nums[i]
            else:
                if(start == end):
                    re.append(str(end))
                else:
                    re.append(str(start) + '->' + str(end))
                start = nums[i]
                end = nums[i]
        
        if(start == end):
            re.append(str(end))
        else:
            re.append(str(start) + '->' + str(end))
        
        return re