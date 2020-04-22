class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        nums.sort()

        re = []

        if(length == 3):
            if(nums[0] + nums[1] + nums[2] == 0):
                return [[nums[0], nums[1], nums[2]]]

        for one in range(length):
            if(nums[one] > 0):
                break
            if(one > 0 and nums[one] == nums[one-1]):
                continue
            two = one + 1
            three = length - 1

            while(two < three):
                sum1 = nums[one] + nums[two] + nums[three]
                if(sum1 > 0):
                    three -= 1
                if(sum1 < 0):
                    two += 1
                if(sum1 == 0):
                    re.append([nums[one], nums[two], nums[three]])
                    while(two < three):
                        if(nums[two] == nums[two+1]):
                            two += 1
                        else:
                            break
                    while(two < three):
                        if(nums[three] == nums[three-1]):
                            three -= 1
                        else:
                            break
                    two += 1
                    three -= 1
        return re