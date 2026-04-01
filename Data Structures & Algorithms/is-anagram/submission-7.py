class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=[0]*26
        b=[0]*26
        for x in s:
            no= ord(x)-ord('a')
            a[no]=a[no]+1
        for x in t:
            no= ord(x)-ord('a')
            b[no]=b[no]+1
        
        if a==b : return True 
        else: return False
