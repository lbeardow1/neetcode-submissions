class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        day = []
        for i in range(len(temperatures)):
            found = False
            total_days = -1
            for j in range(i,len(temperatures)):
                total_days +=1
                print(temperatures[i])
                print(temperatures[j])
                if temperatures[j] > temperatures[i]:
                    day.append(total_days)
                    found = True
                    break
            if not found:
                day.append(0)
                    
        return day
                
        