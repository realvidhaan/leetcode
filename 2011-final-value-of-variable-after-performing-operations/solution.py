class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for digit in operations:
            if digit == '--X' or digit == 'X--':
                x -= 1
            else:
                x +=1
        return x
