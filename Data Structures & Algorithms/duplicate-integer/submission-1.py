class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique=set()
        n=len(nums)

        for c in nums:
            if c in unique:
                return True
            unique.add(c)
        
        return  False
        
        