class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        reverse = []
        for i in nums:
            reverse.append(int(str(i)[::-1]))
        return len(set(reverse+nums))