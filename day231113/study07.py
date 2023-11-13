import numpy as np

# 35~74 까지의 순차적인 수로 이루어진 1차원 배열 만들고, 10x4 행렬로 변환
arr = np.arange(35, 75)
arr2 = arr.reshape(10,4)

print("#6 :\n", arr2)

# 맨끝부터 역순 출력
print("#7 :\n", (arr2[::-1]) )

# 2번쨰 행부터 마지막전 행까지, 세번째열부터 마지막열까지 슬라이싱 출력
print("#8 :\n", arr2[ 1:(arr2.shape[0]-1), 2: ])

# 마지막 열에 해당하는 값, (1차원)
print("#9 :\n", arr2[:, -1:].flatten())

# 마지막 열에 해당하는 값, (2차원)
arr3 = arr2[:, -1:].reshape(len(arr2),1)
print("9-1 :\n", arr3) 

# 9-1번 문제 역순 출력하기
print("#10 : \n", arr3[::-1])

# 1~50 난수로 된 배열 5x6을 만들고 배열에서 짝수만 선택해서 출력
arr4 = np.random.randint(1, 51, size=(5,6))
print(arr4)
print(arr4[arr4%2==0])