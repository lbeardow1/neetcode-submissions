# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
import random
class Solution:
    def guessNumber(self, n: int) -> int:

        min = 0
        max = ((2**31)-1)

        while True:
            number = random.randint(min,max)

            if guess(number) == 0:
                return number
            elif guess(number) == -1:
                max = number - 1
            else:
                min = number + 1


            


        