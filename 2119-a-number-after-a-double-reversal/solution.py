class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        elif int(str(num)[-1]) == 0:
            return False
        return True