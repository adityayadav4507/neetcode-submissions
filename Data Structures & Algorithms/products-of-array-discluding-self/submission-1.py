class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prev=[0]*n
        suff=[0]*n

    ## 1. product of previous indexs
        p=1
        for i in range(n):
            p=p*nums[i]
            prev[i]=p
    ## 2. product of suffix indexs
        p=1
        for i in range(n-1,-1,-1):
            p=p*nums[i]
            suff[i]=p
    ## 3. product except current index
        ans=[0]*n
        for i in range(n):
            if i == 0: p_prev=1
            else: p_prev=prev[i-1]

            if i == n-1 : p_suff=1
            else: p_suff=suff[i+1]

            ans[i]= p_suff * p_prev
        
        return ans


        


       

        