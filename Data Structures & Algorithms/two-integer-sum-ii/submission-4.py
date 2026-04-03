class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx1, idx2 = 0, None
        for i in range(len(numbers)):
            idx1 = i
            j = i+1
            while j < len(numbers):
                if numbers[j] == target - numbers[i]:
                    idx2 = j
                    break
                j += 1
            if idx2 is not None:
                break

        return [idx1+1, idx2+1]
