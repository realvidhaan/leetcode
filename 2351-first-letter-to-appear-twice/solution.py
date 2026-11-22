class Solution:
    def repeatedCharacter(self, s: str) -> str:
        sets=set()
        for i in s:
            if i in sets:
                return i
            sets.add(i)
        return ""