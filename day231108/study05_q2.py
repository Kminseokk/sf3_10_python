num_1 = input("첫 세자리 숫자를 입력하세요.")
num_2 = input("두 세자리 숫자를 입력하세요.")

int_num_1 = int(num_1)
int_num_2 = list(num_2)
# int_num_2 = int(num_2)

print(int_num_1 * int(int_num_2[2]))
print(int_num_1 * int(int_num_2[1]))
print(int_num_1 * int(int_num_2[0]))

first = int_num_1 * int(int_num_2[2])
secon = int_num_1 * int(int_num_2[1]) * 10
third = int_num_1 * int(int_num_2[0]) * 100

print (first + secon + third)
