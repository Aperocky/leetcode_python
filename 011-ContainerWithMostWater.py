"""

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2. 

This does not require the all lines in between be the biggest.

"""

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Use two pointer method.
        maxarea = 0
        i, j = 0, len(height) - 1
        while True:
            if i == j:
                break
            h = min(height[i], height[j])
            maxarea = max(maxarea, h*(j-i))
            if height[i] >= height[j]:
                j -= 1
            else:
                i += 1
        return maxarea

# 71.00%