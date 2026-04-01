class Solution:
    def reverse(self, x: int) -> int:
        y=0

        if x>0:
         while x:
            y=y*10
            y=y+x%10
            x=int(x/10)

         if y > pow(2,31)-1:
            return 0
         else:
            return y
        else:
           x=-x
           while x:
             y=y*10
             y=y+x%10
             x=int(x/10)
           y=-y
           if y < -pow(2,31):
             return 0
           else:
             return y

    
        
        
        