class Solution:
    def countEven(self, num: int) -> int:
        counter=0
        for i in range(1, num+1):
            if sum([int(digit) for digit in str(abs(i))])%2==0:
                counter+=1
        return counter