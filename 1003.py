class fbnc:
    value=0
    value_0=0
    value_1=0
    
    def __init__(self,value):
        self.value=value
        
    def fibonacci(self):
        if self.value==0:
            self.value_0=self.value_0+1
            return 0
        elif self.value==1:
            self.value_1=self.value_1+1
            return 1
        else:
            return self.fibonacci(self.value-1)+self.fibonacci(self.value-2)

    def prt(self):
        print self.value_0,self.value_1
    
if __name__=='__main__':
    time=int(raw_input())
    for a in range(time):
        in_value=int(raw_input())
        obj=fbnc(in_value)
        obj.fibonacci()
        obj.prt()
