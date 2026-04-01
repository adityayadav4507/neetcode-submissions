class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s=set()
        sm=0
        for i in range(len(nums)):
            s.add(nums[i])
            sm+=nums[i]
        
        return 2*sum(s)-sm
        