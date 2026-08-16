class Solution:
    def minElement(self, nums: List[int]) -> int:
        lst = []
        for i in nums:
            lst.append(sum([int(digit) for digit in str(abs(i))]))
        return min(lst)