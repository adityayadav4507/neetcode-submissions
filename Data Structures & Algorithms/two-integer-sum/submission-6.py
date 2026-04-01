class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[i]+nums[j+i+1]==target:
                    ans=[i,j+i+1]
                    return ans
        