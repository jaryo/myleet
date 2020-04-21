class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        length = len(nums)
        temp = []

        for i in range(length):
            if (nums[i] % 2 != 0):
                temp.append(i)

        re = 0

        for i in range(len(temp)):
            a = 1
            b = 1

            if(i + k > len(temp)):
                break

            if (i + k < len(temp)):
                b = temp[i+k] - temp[i+k-1] - 1
            else:
                if(i + k == len(temp)):
                    b = length - temp[i+k-1] -1

            if (i == 0):
                a = temp[i]
            else:
                 a = temp[i] - temp[i-1] - 1

            re += a * b + a + b + 1

        return re