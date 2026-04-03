class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_k = []
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1
        freq_n_map = {}
        for n in freq:
            if freq[n] not in freq_n_map:
                freq_n_map[freq[n]] = [n]
            else:
                freq_n_map[freq[n]].append(n)
        
        while(len(top_k)) < k:
            max_f = max(freq_n_map)
            top_k.extend(freq_n_map[max_f][:k])
            del freq_n_map[max_f]
        return top_k

