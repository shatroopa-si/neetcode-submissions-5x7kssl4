class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        if len(height) <= 2 or height is None:
            return area

        prefix, suffix = [0] * len(height), [0] * len(height)
        for i in range(1, len(height)):
            prefix[i] = max(prefix[i-1], height[i-1])
        for i in range(len(height)-2, -1, -1):
            suffix[i] = max(suffix[i+1], height[i+1])
        print(prefix, suffix)
        i = 1
        while i<len(height)-1:
            diff = min(prefix[i], suffix[i]) - height[i]
            area += diff if diff > 0 else 0
            i += 1

        return area