class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        counts={}
        for i in range(len(numbers)):
            val=target - numbers[i]
            index=counts.get(val,-1)
            if index != -1 :
                ans=[index+1,i+1]
                return ans
            else:
                counts[numbers[i]]=i

        