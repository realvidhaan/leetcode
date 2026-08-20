class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        lst = []
        for i in str(x):
            lst.append(int(i))
        if x%sum(lst) ==0:
            return sum(lst)
        return -1