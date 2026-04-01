class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a={}

        for x in s :
            if x in a:
                a[x]+=1
            else: a[x]=1
        
        b={}
        for y in t :
            if y in b:
                b[y]+=1
            else: b[y]=1
        
        if a==b: return True
        else: return False
        