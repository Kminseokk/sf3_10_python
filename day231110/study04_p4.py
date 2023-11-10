
class calc() :
    a = 0
    b = 0

    def __init__(self,a, b) :
        self.a = a
        self.b = b
        print("생성자")

    def add(self) :
        return self.a + self.b
    
    def sub(self) :
        return self.a - self.b
    
    def mul(self) :
        return self.a * self.b

    def div(self) :
        return self.a / self.b

calc1 = calc(10, 20)

print( calc1.add() )
