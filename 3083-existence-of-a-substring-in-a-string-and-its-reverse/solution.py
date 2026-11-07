class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        substrings = []
        for start in range(len(s)):
            for end in range(start, len(s)):
                substrings.append(s[start:end + 1])
        for i in substrings:
            if i in s[::-1] and len(i)==2:
                return True
        return False