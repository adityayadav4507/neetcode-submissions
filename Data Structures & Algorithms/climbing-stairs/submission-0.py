

class Solution:
    def rec(self,n:int)->int:
        ## base case 
        if n==1:
            return 1
        if n==2:
            return 2 
        return self.rec(n-1) + self.rec(n-2)
    def climbStairs(self, n: int) -> int:

        return self.rec(n)

        