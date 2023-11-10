
vending_ms = ['게토레이','게토레이','레쓰비','레쓰비','생수','생수','생수','이프로']

choice = 0

def check_machine():
    print(vending_ms)

def is_drink(choice):
    if choice in vending_ms :
        print(f"{choice} 드릴게요")
        vending_ms.remove(choice)
    else :
        print(f"{choice} 없어용")

def add_drink(task):
    choice = input("추가할 음료 : ")
    vending_ms.append(choice)
    vending_ms.sort()
    print(f"{choice} 추가 완료")

def del_drink(task):
    choice = input("삭제할 음료 : ")
    vending_ms.remove(choice)
    print(f"{choice} 삭제 완료")

def main_work():
    iam = input("사용자는 누구입니까? \n1.소비자 \n2.주인\n")
    user_work(iam)

def error_msg(x):
    print(f"{x}는 올바르지 못한 요청입니다.")

def user_work(iam):
    # 손님일때 iam = 1
    if iam == "1" :        
        check_machine()
        choice = input("마실 음료? : ")
        is_drink(choice)

    # 주인일때 iam = 2
    elif iam == "2" :
        task = input("할 일 선택 : \n1.추가 \n2.삭제\n")
        
        if task == "1" :
            add_drink(task)
        elif task == "2" :
            del_drink(task)
        else:
            error_msg(task)


print("============시작해볼까============")
while True :    
    check_machine()
    main_work()

    print("============다시 시작하기전 재고 확인============")
    check_machine()
    print("============다시 시작합니다============")


