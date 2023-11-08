
num = int(input("점수 입력해주세용 : "))

if 90 <= num <= 100 :
    print("A등급")
elif 80 <= num < 90 :
    print("B등급")
elif 70 <= num < 80 :
    print("C등급")
elif 60 <= num < 70 :
    print("D등급")
elif num < 60 :
    print("E등급")
else :
    print("점수를 잘못입력함")
