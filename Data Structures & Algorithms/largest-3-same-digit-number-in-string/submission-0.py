class Solution:
    def largestGoodInteger(self, num: str) -> str:

        answer = []

        if len(num) < 3:
            return ""

        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                answer.append(num[i]*3)

        if len(answer) == 0:
            return ""
        
        return max(answer)



