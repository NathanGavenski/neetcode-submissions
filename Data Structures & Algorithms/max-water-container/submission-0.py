class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for i, left in enumerate(heights):
            for j, right in enumerate(heights[i+1:]):
                current = (j+1) * min(left, right)
                if max_area < current:
                    max_area =  current
        return max_area