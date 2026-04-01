class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=set()
        for x in nums: s.add(x)

        if len(nums)==len(s) : return False
        else: return True
        