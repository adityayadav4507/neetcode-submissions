

class Solution:
    def rec(self,n:int,memo: dict)->int:
        ## base case 
        if n in memo :
            return memo[n]
        if n==1:
            return 1
        if n==2:
            return 2 
        memo[n]= self.rec(n-1,memo) + self.rec(n-2,memo)
        return memo[n]
    def climbStairs(self, n: int) -> int:
        memo={}
        return self.rec(n,memo)

        