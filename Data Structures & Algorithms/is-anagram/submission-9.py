class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a={}
        b={}
        for x in s:
            if x in a : a[x]=a[x]+1
            else: a[x]=1

        for x in t:
            if x in b : b[x]=b[x]+1
            else: b[x]=1

        if a==b : return True
        else: return False