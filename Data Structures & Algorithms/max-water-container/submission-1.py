class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area, max_area = 0, 0
        s, e = 0, len(heights) - 1
        while s < e:
            area = min(heights[s], heights[e]) * (e-s)
            max_area = max(area, max_area)
            if heights[s] < heights[e]:
                s += 1
            else:
                e = e - 1
        return max_area