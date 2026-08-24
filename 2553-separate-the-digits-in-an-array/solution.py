class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        lst = []
        for i in nums:
            for j in str(i):
                lst.append(int(j))
        return lst