class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        lst = []
        for i in nums:
            if nums.count(i)==2:
                lst.append(i)
        if len(lst)==0:
            return 0
        return reduce(lambda x, y: x ^ y, list(set(lst)))