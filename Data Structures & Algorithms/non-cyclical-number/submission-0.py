class Solution:
    def isHappy(self, n: int) -> bool:
        
        visit=set()

        while n not in visit:
            visit.add(n)
            n=self.issum(n)
            if n==1:
             return True
        
        return False
    
    def issum(self,n: int) -> int:
        sum=0
        while n:
            x=n%10
            sum=sum+x**2
            n=int(n/10)
        return sum


        