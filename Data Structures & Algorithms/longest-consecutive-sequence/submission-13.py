from collections import Counter
import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
            Total run time: O(n)
            Space: O(n)

            Input: Neither sorted nor unique
        """
        # Sanity check
        if len(nums) < 1:
            return 0
        
        # Find all unique elements and build from min to max
        nums_map = Counter(nums)
        len_n = len(nums)
        begin = min(nums)
        max_count, count = 1 if len(nums) >= 1 else 0, 1
        for n in nums:
            if n - 1 not in nums_map:
                begin = n
                count = 1
                while begin + 1 in nums_map:
                    count += 1
                    begin += 1
                max_count = max(count, max_count)        
        return max_count


    def longestConsecutiveLinearithmic(self, nums: List[int]) -> int:
        """
            Total run time: O(n log n)
            Space: O(1); Not using any extra space; in-place heapify

            Input: Neither sorted nor unique
        """
        # Sanity check
        if len(nums) < 1:
            return 0
        
        # Find all unique elements and build from min to max
        heapq.heapify(nums)             # linear time; doesn't sort
        begin = heapq.heappop(nums)
        max_count, count = 1 if len(nums) >=1 else 0, 1
        while nums:
            n = heapq.heappop(nums)      # O(log n)
            if begin + 1 == n:
                count += 1
                begin += 1
            elif begin == n:
                continue
            else:
                max_count = max(count, max_count)
                count = 1
                begin = n
        return max_count
        
            