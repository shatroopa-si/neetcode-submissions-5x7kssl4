class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Check input
        if len(nums) == 0:
            return False

        # Count frequency
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        # Check if any frequency is more than 1
        if any(freq[n] > 1 for n in freq):
            return True
        return False