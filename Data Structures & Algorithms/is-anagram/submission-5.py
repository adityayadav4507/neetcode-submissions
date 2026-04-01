class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        a=[0]*26 # array of size 26 all value are 0 
        for x in s:
          a[ord(x)-ord('a')] +=1

        b=[0]*26
        for y in t:
            b[ord(y)-ord('a')]+=1
        
        if a==b : return True
        else: return False


        
        