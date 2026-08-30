from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        max_value = 0

        for key, value in count.items():
            if key == value:
                max_value = max(max_value,key) 
        
        if max_value == 0:
            return -1
        else:
            return max_value


        