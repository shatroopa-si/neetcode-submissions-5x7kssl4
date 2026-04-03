class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k==1:
            return nums
        
        n = len(nums)
        w = nums[: k]
        max_w = [max(w)]
        for i in range(1, n-k+1):
            max_w.append(max(nums[i:i+k]))
        return max_w
