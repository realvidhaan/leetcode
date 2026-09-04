class Solution:
    def averageValue(self, nums: List[int]) -> int:
        lst = []
        for i in nums:
            if i%6==0:
                lst.append(i)
        if len(lst)>0:
            return int(sum(lst)/len(lst))
        return 0