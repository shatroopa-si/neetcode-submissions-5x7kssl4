class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_idx_map = {}
        for i, n in enumerate(nums):
            x = target - n
            if x in n_idx_map and i != n_idx_map[x]:
                op = [i, n_idx_map[x]]
                op.sort()
                return op
            n_idx_map[n] = i