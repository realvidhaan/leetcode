class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        lst = []
        for i in range(0, len(candies)):
            if candies[i] + extraCandies >= max(candies):
                lst.append(True)
            else:
                lst.append(False)
        return lst
        