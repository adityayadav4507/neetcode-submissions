class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=set()
        for i in range(len(nums)):
            a.add(nums[i])
        
        if len(a)==len(nums):return False
        else: return True 

        