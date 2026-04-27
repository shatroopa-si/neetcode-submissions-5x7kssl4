class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## nums is not necessarily sorted
        # Create hash map: {value: most recent index in nums]}
        nums_map = {}

        # Search for sum of 2 numbers == target
        i = 0               # iterator
        while i < len(nums):
            diff = target - nums[i]
            
            # Given that there is only one output pair
            if diff in nums_map:
                j = nums_map[diff]
                return [j, i]
            
            nums_map[nums[i]] = i
            i += 1

        