class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, n+10):
            s = []
            for j in str(i):
                s.append(int(j))
            if math.prod(s)==0 or math.prod(s)%t==0:
                return i