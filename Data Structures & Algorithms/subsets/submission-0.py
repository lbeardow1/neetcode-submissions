class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        addition = []
        for num in nums:
            result += [curr + [num] for curr in result]
        return result