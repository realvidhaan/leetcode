class Solution:
    def countDigits(self, num: int) -> int:
        counter = 0
        for digit in [int(i) for i in str(num)]:
            if num%digit==0:
                counter+=1
        return counter
