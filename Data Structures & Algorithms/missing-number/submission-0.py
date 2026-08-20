class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        complete_set = list(range(0,(len(nums)+1)))
        return (set(complete_set) - set(nums)).pop()