class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prod = [1] # Accumulate product of all elements before i
        suf_prod = [1] # Accumulate product of all elements after i
        n = len(nums)

        i = 1
        while i < n:
            pre_prod.append(pre_prod[i-1] * nums[i-1])
            i += 1

        i = n - 1
        while i > 0:
            suf_prod = [suf_prod[0] * nums[i]] + suf_prod
            i -= 1

        # Compute product except self by multiplying prefix and suffix products.        
        prod_exc_self = [p * s for p, s in zip(pre_prod, suf_prod)]
        return prod_exc_self