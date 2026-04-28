class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        
        leftmax = heights[0]
        rightmax = heights[right]

        water = 0
        maxwater=0

        while left<right:
            if heights[left]<=heights[right]:
                water = (heights[left])*(right-left)
                if maxwater < water:
                    maxwater = water
                left += 1
            else:
                water = heights[right] * (right-left)
                if maxwater < water:
                    maxwater = water
                right -= 1
        return maxwater