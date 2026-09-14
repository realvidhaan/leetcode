class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        counter = 0
        for i in list(combinations(hours, 2)):
            if sum(i)%24==0:
                counter+=1
        return counter