class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        re = []
        use = [0 for x in range(len(nums))]
        temp = []

        def backtrack(nums, use):
            if(len(temp) == len(nums)):
                re.append(temp[:])
                return
            
            for i in range(len(nums)):
                if(use[i] == 0):
                    #这里，当前数字与前一个数字相同且前一个数字没用过，说明当前的是之前用过的重复数字，去重
                    if(i > 0 and nums[i] == nums[i-1] and use[i-1] == 0):
                        continue
                    temp.append(nums[i])
                    use[i] = 1
                    backtrack(nums, use)
                    temp.pop()
                    use[i] = 0
        
        nums.sort()
        backtrack(nums, use)

        return re