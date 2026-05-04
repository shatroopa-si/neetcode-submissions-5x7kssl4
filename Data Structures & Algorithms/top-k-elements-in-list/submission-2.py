import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_k = []
        freq = Counter(nums)
        freq_n_map = {}
        for n in freq:
            if freq[n] not in freq_n_map:
                freq_n_map[freq[n]] = [n]
            else:
                freq_n_map[freq[n]].append(n)
        
        heap = list(freq_n_map.keys())
        heap = [h * -1 for h in heap]
        
        heapq.heapify(heap)

        while(len(top_k)) < k:
            max_f = heapq.heappop(heap) * -1             # O(log k)
            top_k.extend(freq_n_map[max_f][:k-len(top_k)])
            del freq_n_map[max_f]

        return top_k

