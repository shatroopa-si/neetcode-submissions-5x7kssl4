class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq_nums = set(nums)
        length, max_length = 0, 0
        for n in uniq_nums:
            if n - 1 not in uniq_nums:          # begin a new sequence
                length = 1
                while n+1 in uniq_nums:
                    n = n+1
                    length += 1
                max_length = max(length, max_length)
        return max_length
