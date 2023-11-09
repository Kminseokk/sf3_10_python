
input_num = input("숫자 여러개 입력 : ")

list_num = input_num.split(" ")

list_num.remove(max(list_num))
list_num.remove(min(list_num))
list_num.sort()

num = len(list_num)
print("젤 작음 = ", list_num[0])
print("젤 큼 = ",list_num[num-1])

sum = 0
for i in range(0, num) :
    #print(list_num[i])
    sum += int(list_num[i])

print("평균 = ", sum/num)