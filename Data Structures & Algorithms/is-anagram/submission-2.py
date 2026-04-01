class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map={}

        if len(s) != len(t):
            return False
        
        for c in s:
            map[c]=1+map.get(c,0)
        
        for c in t:
            if c not in map:
                return False
            map[c]=map.get(c)-1
            
            if map.get(c) < 0:
                return False
        
        return True
        
        

        