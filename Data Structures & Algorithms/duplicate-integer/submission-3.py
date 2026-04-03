class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        p_freq, n_freq = [], []
        p_size, n_size = max(nums) + 1, abs(min(nums)) + 1
        for i in range(p_size):
            p_freq.append(0)
        for i in range(n_size):
            n_freq.append(0)
        for n in nums:
            if n >= 0:
                p_freq[n] += 1
            else:
                n_freq[abs(n)] += 1

        is_duplicate = False
        if any([f > 1 for f in p_freq]):
            is_duplicate = True
        elif any([f > 1 for f in n_freq]):
            is_duplicate = True
        
        return is_duplicate
         