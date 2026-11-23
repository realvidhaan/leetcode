class Solution:
    def similarPairs(self, words: List[str]) -> int:
        counter=0
        for i in list(combinations(words, 2)):
            if sorted(set(i[0]))==sorted(set(i[1])):
                counter+=1
        return counter