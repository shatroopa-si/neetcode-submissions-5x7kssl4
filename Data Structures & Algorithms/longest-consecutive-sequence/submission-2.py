class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or nums is None:
            return 0
        freq_nums = {}
        for n in nums:
            freq_nums[n] = 1 if n not in freq_nums else freq_nums[n] + 1
        
        length, max_length, min_n, max_n = 1, 0, min(freq_nums.keys()), max(freq_nums.keys())
        next_n = min_n + 1
        while next_n <= max_n:
            if next_n in freq_nums:
                length += 1
                next_n = next_n + 1
            else:
                if length > max_length:
                    max_length = length
                length = 0
                next_n = next_n + 1
        if length > max_length:
            max_length = length
        return max_length