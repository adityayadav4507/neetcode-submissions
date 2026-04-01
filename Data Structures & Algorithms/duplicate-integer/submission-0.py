class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique=set()
        n=len(nums)

        for c in nums:
            unique.add(c)
        
        return  n!=len(unique)
        
        