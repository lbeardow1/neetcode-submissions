class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        answer = []
        current_max = 0
        for i in range(len(arr)-1):
            
            for j in range (i+1,len(arr)):
                if arr[j] > current_max:
                    current_max = arr[j]
                    print(current_max)
            answer.append(current_max)
            current_max = 0
        answer.insert(len(arr)-1,-1)
        return answer

        