class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        change = False

        for i in range(1, length)[::-1]: #倒着找到一个可以交换的位置，说明不是递减序列，将该位置后的比前一位置大的最小值与前一位置交换，然后将该位置后进行排序即可
            if (nums[i] > nums[i - 1]):
                minp = i
                for j in range(i + 1, length):
                    if (nums[j] < nums[minp] and nums[j] > nums[i - 1]): 
                        minp = j
                nums[minp], nums[i-1] = nums[i-1], nums[minp]
                nums[i:] = sorted(nums[i:]) 
                change = True
                break
        if(not change):
            nums[:] = nums[::-1]