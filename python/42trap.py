class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
        	return 0
        leftMax, rightMax = height[0], height[-1]
        left, right = 1, len(height) - 2
        res = 0
        while left <= right:
        	if leftMax <= rightMax:
        		if height[left] >= leftMax:
        			leftMax = height[left]
        		else:
        			res += (leftMax - height[left])
        		left += 1
        	else:
        		if height[right] >= rightMax:
        			rightMax = height[right]
        		else:
        			res += (rightMax - height[right])
        		right -= 1
        return res