
num = int(input("어디까지 계산? : "))

summ = 0

for i in range(1, num+1) :
    summ += i
print("포문 썸", summ)

ab_sum = 0
for i in range(1, num +1, 2) :
    ab_sum += i
print("포문에서 홀수만", ab_sum)

no_sum = 0
no_sum = sum(range(1, num + 1, 2))
print("포문은 홀수만 안쓰고", no_sum)

##### 
print("test22")