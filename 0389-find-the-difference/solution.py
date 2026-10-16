class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s1= []
        t1 =[]
        for i in s:
            s1.append(ord(i))
        for j in t:
            t1.append(ord(j))
        return chr(abs(sum(t1)-sum(s1)))