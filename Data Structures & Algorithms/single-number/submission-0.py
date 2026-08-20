class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        going = set()
        duplicates = set()
        for i in nums:
            if i in going:
                duplicates.add(i)
            else:
                going.add(i)
                
        return list(going - duplicates)[0]