class Calculator:
    def add(self, a , b):
        print(a+b)
        return
    
    def sub(self, a , b):
        print(a-b)
        return
    
    def multi(self, a , b):
        print (a*b)
        return
    
    def div(self, a , b):
        if(b == 0):
            print("INFNITY!")
            return
        else:
            print(a/b)
            return
    

calc = Calculator()

calc.add(1,2)
calc.sub(2,1)
calc.multi(2,10)
calc.div(25,5)
calc.div(25,0)