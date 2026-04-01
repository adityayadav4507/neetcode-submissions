class Solution:
    def isPalindrome(self, s: str) -> bool:
        r=[]
        l=[]
        s=s.lower()

        for x in s :
           if 'a'<=x<='z' or 'A'<=x<='Z' or '0'<=x<='9':
              l.append(x)
        for i in range(len(s)-1,-1,-1):
           x=s[i]
           if 'a'<=x<='z' or 'A'<=x<='Z' or '0'<=x<='9':
              r.append(x)
        print(l)
        print(r)
        if r==l : return True
        else: return False