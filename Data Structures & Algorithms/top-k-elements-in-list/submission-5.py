from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
            Inspired from bucket sort. 
            T(n) = O(n); S(n) = O(n).
        """
        top_k = []
        freq = Counter(nums)
        count_nums = len(nums)
        freq_n_map = [[] for _ in range(count_nums + 1)]
        # creating buckets for every frequency
        for n, f in freq.items():
            freq_n_map[f].append(n)
        
        # fetch the top k most frequent numbers by fetching from the array in reverse order
        f = count_nums
        while len(top_k) < k and f >= 0:
            top_k.extend(freq_n_map[f])
            f -= 1

        return top_k

