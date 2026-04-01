class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=[]

        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                x=target-nums[i]
                if x==nums[j]:
                    a.append(i)
                    a.append(j)
                    return a