import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        for i in range(len(nums)):
            removed = nums[i]
            nums.pop(i)
            products.append(math.prod(nums))
            nums.insert(i,removed)
            
        return products
            
        