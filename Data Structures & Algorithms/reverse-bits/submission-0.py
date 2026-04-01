class Solution:
    def reverseBits(self, n: int) -> int:

        s=0
        for i in range(32):
            no=n&1
            s+=no*pow(2,31-i)
            n=n>>1
        return s

        