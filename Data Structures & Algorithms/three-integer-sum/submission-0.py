class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        zero_triplets = set()
        for i in range(len(nums)-2):
            j, k = i+1, len(nums) - 1
            target = 0 - nums[i]
            while k > j:
                if nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] == target:
                    zero_triplets.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
        
        return list(zero_triplets)





        