class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        a={}
        for i,val in enumerate(nums):
            x=target-val
            if x in a : return [a[x],i]
            else: a[val]=i

        