class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## 1. making dic to store counts of anagram
        a={}
        for x in strs:
            y=str(sorted(x))
            if y in a : a[y]=a[y]+1
            else: a[y]=1
        
        ## 2. append the anagram string
        ans=[]
        for string in strs:
            sorted_string=str(sorted(string))
            s=[]    # list of anagram
            for x in strs:
                if str(sorted(x))==sorted_string:
                    s.append(x)
            if s  not in ans : ans.append(s)
        
        return ans


                
        