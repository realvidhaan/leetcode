class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        odd=[]
        even=[]
        for i in nums:
            if len(str(i)) == 1:
                even.append(i)
            else:
                odd.append(i)
        return sum(odd)!=sum(even)
           