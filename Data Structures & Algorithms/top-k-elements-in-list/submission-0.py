class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        a={}
        for x in nums:
            if x in a :
                a[x]=a[x]+1
            else: a[x]=1
        
        ans=[]
        a=dict(sorted(a.items(), key=lambda x:x[1], reverse=True))
        
        for key in a:
             if k > 0:
               ans.append(key)
               k-=1

        return ans