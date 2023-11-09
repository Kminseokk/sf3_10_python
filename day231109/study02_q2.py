
vending_ms = ['게토레이','게토레이','레쓰비','레쓰비','생수','생수','생수','이프로']

print("============시작해볼까============")
while True :
    print(vending_ms)
    iam = input("사용자는 누구입니까? \n1.소비자 \n2.주인\n")
    if iam == "주인" or iam == "2" :
        task = input("할 일 선택 : \n1.추가 \n2.삭제\n")        

        if task == "삭제" or task == "2" :
            choice = input("삭제할 음료 : ")
            vending_ms.remove(choice)
            print(f"{choice} 삭제 완료")

        elif task == "추가" or task == "1" :
            choice = input("추가할 음료 : ")
            vending_ms.append(choice)
            vending_ms.sort()
            print(f"{choice} 추가 완료")
        else :
            print(f"{task} 할 일을 잘못 입력하셨습")

    elif iam == "소비자" or iam == "1" :
        choice = input("마실 음료? : ")

        if choice in vending_ms :
            print(f"{choice} 드릴게요")
            vending_ms.remove(choice)
        else :
            print(f"{choice} 없어용")
    
    elif iam == "exit" : 
        break
    else :
        print(f"{iam} 은 사람이 아닙니다.")

    print("남은 음료수 = ", vending_ms)
    print("============다시 시작해볼까============")


