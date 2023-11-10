
class calc() :
    def __init__(self) :
        self.value = 100

    def sub(self, value) :
        self.value -= value

class MinLimitClac(calc) :
    def sub(self, value) :
        self.value -= value
        if self.value < 0 :
            print("음수 ㄴㄴ")
            self.value = 0

cal = MinLimitClac()
cal.sub(20)
cal.sub(90) # 음수 ㄴㄴ 출력
print(cal.value) # 0 출력