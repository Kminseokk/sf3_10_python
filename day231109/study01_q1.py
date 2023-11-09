
n = int(input("정수 n을 입력해 주세요: "))

Q1_list = list(range(1, n+1))
print("전체 리스트 : " , Q1_list)


print("홀수 리스트 : " , Q1_list[0::2])
print("짝수 리스트 : " , Q1_list[1::2])