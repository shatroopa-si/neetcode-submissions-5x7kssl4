class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or nums is None:
            return 0
        unique_nums = set(nums)
        length, max_length, min_n, max_n = 1, 0, min(unique_nums), max(unique_nums)
        next_n = min_n + 1
        while next_n <= max_n:
            if next_n in unique_nums:
                length += 1
            else:
                if length > max_length:
                    max_length = length
                length = 0
            next_n = next_n + 1
        if length > max_length:
            max_length = length
        return max_length
        
        
        