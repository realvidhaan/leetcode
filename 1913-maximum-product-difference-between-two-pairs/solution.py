class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        small = []
        big = []
        small.append(sorted(nums)[0])
        small.append(sorted(nums)[1])
        big.append(sorted(nums)[-1])
        big.append(sorted(nums)[-2])
        return math.prod(big)-math.prod(small)