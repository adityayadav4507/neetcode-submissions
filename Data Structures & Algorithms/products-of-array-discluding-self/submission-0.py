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
            index=i-1
            p_prev=1
            if index < 0: p_prev=1
            else: p_prev=prev[index]

            index=i+1
            p_suff=1
            if index == n: p_suff=1
            else: p_suff=suff[index]

            ans[i]= p_suff * p_prev
        
        return ans


        


       

        