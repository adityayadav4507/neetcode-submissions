class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        a={}
        for i in range(len(nums)):
            a[nums[i]]=i
        
        for i in range(len(nums)):
            s=target - nums[i]
            if s in a and a.get(s) != i:
                return [i,a.get(s)]
        