class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = 0
        max_ones = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                ones += 1
            else:
                max_ones = max(ones, max_ones)
                ones = 0
            max_ones = max(ones, max_ones)
        
        return max_ones
        