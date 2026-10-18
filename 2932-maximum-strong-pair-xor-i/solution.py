class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        lst = []
        s = []
        for i in list(combinations(nums, 2)):
            if abs(i[0]-i[1])<=min(i[0], i[1]):
                lst.append((i))
        for j in lst:
            s.append(j[0]^j[1])
        if len(s)==0:
            return 0
        return max(s)
        
            