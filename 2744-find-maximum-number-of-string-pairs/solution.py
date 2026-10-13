class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        counter = 0
        for i in list(combinations(words, 2)):
            if i[0][::-1]==i[1] or i[1][::-1]==i[0]:
                counter+=1
        return counter