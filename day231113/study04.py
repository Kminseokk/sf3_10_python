
while True :
    try:
        num = int(input("숫자 입력 : "))
    except:
        print("정수가 아님, 정수 입력해요! ")
    else:
        print(f"정수 입력 성공 ! {num}")
        break