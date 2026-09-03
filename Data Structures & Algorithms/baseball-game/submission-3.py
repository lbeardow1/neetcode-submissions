class Solution:
    def calPoints(self, operations: List[str]) -> int:

        answer = []

        for i in range(len(operations)):
            
            if operations[i] == "+":
                answer.append(answer[-1]+answer[-2])
            
            elif operations[i] == "C":
                answer.pop()

            elif operations[i] == "D":
                answer.append(answer[-1]*2)
            
            else:
                answer.append(int(operations[i]))

        print(answer)
        
        return sum(answer)

        