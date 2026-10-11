class Solution:
    def isBalanced(self, num: str) -> bool:
        even=[]
        odd=[]
        for i, j in enumerate(num):
            if i%2==0:
                even.append(int(j))
            else:
                odd.append(int(j))
        return sum(odd)==sum(even)