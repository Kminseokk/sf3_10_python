import numpy as np

# 10개의 0으로 채워진 array 만들기

arr = np.zeros(10)
print("#1 :\n", arr)

# array 의 5번째의 값을 1로 바꾸고 출력

arr[5] = 1
print("#2 :\n", arr)

# 10부터 30까지의 수로 이루어진 array 

arr_1 = np.arange(10,31)
print("#3 :\n", arr_1)

# 0~99 의 난수로 이루어진 2x2 array 

arr_2 = np.random.randint(1,100, size=(2,2) )
print("#4 :\n", arr_2)

# 0~1 사이 난수 2x4 array 

arr_3 = np.random.rand(2,4)
print("#5 :\n", arr_3)

