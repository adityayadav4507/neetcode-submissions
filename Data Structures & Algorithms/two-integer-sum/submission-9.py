class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counts={}
        # using hash map 
        for i in range(len(nums)):
            r=target - nums[i]
            index_r=counts.get(r,-1)           
            if index_r == -1:
                 counts[nums[i]]=i
            else:
                ans=[index_r,i]
                return ans
        