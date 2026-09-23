class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num=0
        for i in range(0, len(set(nums))+1):
            if i not in nums:
                num+=i
        return num