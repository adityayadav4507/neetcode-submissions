class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def summation(n):
            s=0
            while n !=0:
                if n&1 ==1: s+=1
                n=n>>1

            return s
        
        arr=[]
        for i in range(n+1):
            arr.append(summation(i))
        
        return arr
