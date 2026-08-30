class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        lst = []
        for i in nums:
            if nums.count(i) > 1:
                lst.append(i)
        return list(set(lst))
