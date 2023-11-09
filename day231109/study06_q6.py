
lines = int(input("몇 줄 "))

for i in range(1, lines+1) :
    print("*" * i )

for i in range(1, lines+1) :
    print(" " * (lines -i) , "*" * i )

# 1 , 2 4 6 8

for i in range(1, lines+1) :
    print(" " * (lines -i) , "*" * (i*2 -1) )