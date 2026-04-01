class MinStack:

    def __init__(self):
        self.a=[]
        self.a_min=[]
        

    def push(self, val: int) -> None:
        self.a.append(val)
        if not self.a_min:
            self.a_min.append(val)
        else:
            self.a_min.append(min(self.a[-1],self.a_min[-1]))

    def pop(self) -> None:
        self.a.pop(-1)
        self.a_min.pop(-1)

    def top(self) -> int:
        return self.a[-1]
        
    def getMin(self) -> int:
        return self.a_min[-1]


        
