import random

list_a = []

for i in range(4) :
    list_a.append(random.randint(1,100))

list_a.sort()

print(list_a)

#########

ans = random.randint(1,10)

while(1) :
    choice = int(input("숫자를 맞춰"))

    if choice == ans :
        print("정답")
        break
    else:
        print("땡")

#############

lotto = random.sample(range(45), 6)

print(lotto)