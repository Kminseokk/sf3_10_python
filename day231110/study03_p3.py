
fevo = [1,1]

def fevona(n) :
    if n < 2:
        return 1
    
    return fevona(n-1) + fevona(n-2)


# for i in range(40):
#     print(f"{i} 번째 {fevona(i)}" )

memory = {1 : 1, 2: 1}

def fibo(n):
    if n in memory :
        number2 = memory[n]
    else :
        number = fibo(n-1) + fibo(n-2)
        memory[n] = number
    return number2
