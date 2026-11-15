class Solution:
    def isFascinating(self, n: int) -> bool:
        ans = [2*n]
        ans2=[3*n]
        lst=[]
        lst1=[]
        bob=[1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in str(n):
            lst.append(int(i))
        for x in ans:
            for j in str(x):
                lst1.append(int(j))
        for b in ans2:
            for f in str(b):
                lst1.append(int(f))
        return sorted(lst1+lst)==bob