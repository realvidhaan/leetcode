class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        lst = []
        for i in nums:
            if nums.count(i)==1:
                lst.append(i)
        return lst