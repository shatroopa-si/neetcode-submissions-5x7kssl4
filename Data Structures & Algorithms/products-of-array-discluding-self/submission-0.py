class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_product = 1
        for n in nums:
            all_product *= n

        output = []
        for idx, n in enumerate(nums):
            if n != 0:
                output.append(all_product // n)
            else:
                p = 1
                for j in range(len(nums)):
                    if idx != j:
                        p *= nums[j]
                output.append(p)
        return output