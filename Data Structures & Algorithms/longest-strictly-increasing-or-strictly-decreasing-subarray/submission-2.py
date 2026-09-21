class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        count_up = 1
        count_down = 1
        current_up = 1
        current_down = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                current_up += 1
            else:
                count_up = max(current_up, count_up)
                current_up = 1

            if nums[i] > nums[i+1]:
                current_down += 1
            else:
                count_down = max(current_down, count_down)
                current_down = 1
    
        count_up = max(current_up, count_up)
        count_down = max(current_down, count_down)
        return max(count_down, count_up)


        