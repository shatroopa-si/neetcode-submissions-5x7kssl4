class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1] * len(nums)
        suffix_product = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix_product[i] = prefix_product[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            suffix_product[i] = suffix_product[i+1] * nums[i+1]
        products = []
        for p1, p2 in zip(prefix_product, suffix_product):
            products.append(p1 * p2)
        return products