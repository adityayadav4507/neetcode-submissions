class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for c in nums:
            res=res^c
        
        return res
        