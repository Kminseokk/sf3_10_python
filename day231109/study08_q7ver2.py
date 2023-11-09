
input_num = input("숫자 여러개 입력 : ")

list_num = input_num.split(" ")
numlist = list(map(int, list_num))

numlist.remove(max(numlist))
numlist.remove(min(numlist))

print("제일 크은 값", max(numlist))
print("제일 작은 값", min(numlist))

print(sum(numlist)/len(numlist))