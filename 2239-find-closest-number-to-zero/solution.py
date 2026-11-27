class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        lst=[]
        lst1=[]
        for i in nums:
            lst.append(abs(i))
        for x in nums:
            if abs(x)==min(lst):
                lst1.append(x)
        return max(lst1)