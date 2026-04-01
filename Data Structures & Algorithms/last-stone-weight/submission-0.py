class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=sorted(stones)
        while len(stones)>1:     
            d=stones[-1]-stones[-2]
            stones.pop()
            if d==0:
                stones.pop()
            else:
                stones[-1]=d
            stones=sorted(stones)
        
        if len(stones)==0:
            return 0
        else:
            return stones[0]


        