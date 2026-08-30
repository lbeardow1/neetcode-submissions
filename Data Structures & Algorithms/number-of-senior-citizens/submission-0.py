class Solution:
    def countSeniors(self, details: List[str]) -> int:
        seniors = 0
        for i in range(len(details)):
            if int(details[i][11:13]) > 60:
                seniors += 1
        return seniors


        