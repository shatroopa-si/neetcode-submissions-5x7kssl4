class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## nums is not necessarily sorted
        # Create hash map: {value: [indices in nums]}
        nums_map = {}
        # i = 0               # iterator
        # while i < len(nums):
        #     n = nums[i]
        #     if n in nums_map:
        #         nums_map[n].append(i)
        #     else:
        #         nums_map[n] = [i]
        #     i += 1

        # Search for sum of 2 numbers == target
        i = 0               # iterator
        while i < len(nums):
            diff = target - nums[i]
            
            # Given that there is only one output pair
            if diff in nums_map:
                j = nums_map[diff]
                if j != i:
                    return [j, i]
            
            nums_map[nums[i]] = i
            i += 1

        