class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        a={}
        for i,x in enumerate(nums):
            a[x]=i
        
        for i in range(len(nums)):
            x=target-nums[i]
            if x in a and a[x] != i : return [i,a[x]]
        