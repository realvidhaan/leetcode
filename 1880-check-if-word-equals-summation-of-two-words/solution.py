class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        w = ""
        l=""
        b=""
        for i in firstWord:
            w+=str(ord(i) - ord('a'))
        for j in secondWord:
            l+=str(ord(j) - ord('a'))
        for x in targetWord:
            b+=str(ord(x) - ord('a'))
        return int(w)+int(l)==int(b)