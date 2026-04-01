class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counts={}
        for i in range(len(nums)):
            counts[nums[i]]=i
        
        # using hash map 
        for i in range(len(nums)):
            r=target-nums[i]
            index_r=counts.get(r,-1)
            if index_r != -1 and i != index_r:
                ans=[i,index_r]
                return ans
        