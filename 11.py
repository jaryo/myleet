class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)

        left = 0
        right = length - 1

        area = 0
        # area = min(height[i],height[j])*(abs(j - i))
        while left < right:
            area = max(area, min(height[left],height[right])*(right - left))

            if(height[left] <= height[right]):
                left = left + 1
            else:
                right = right - 1
        
        return area