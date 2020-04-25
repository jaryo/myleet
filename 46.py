class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        re = []
        temp = []

        def backtrack(nums, temp):
            if(len(temp) == len(nums)):
                re.append(temp[:])
                return
            
            for i in range(len(nums)):
                if(nums[i] in temp):
                    continue
                temp.append(nums[i])
                backtrack(nums, temp)
                temp.remove(nums[i])
        
        backtrack(nums, temp)

        return re