class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        substrings = []
        counter=0
        for start in range(len(s)):
            for end in range(start, len(s)):
                substrings.append(s[start:end + 1])
        for i in substrings:
            if len(set(i))==len(i) and len(i)==3:
                counter+=1
        return counter