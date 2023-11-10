
class supermarket():
    # loca = "" # 장소
    # name = ""  # 가게 이름
    # product = "" # 파는 물건
    # cust = 0 # 고객의 수
    inst_cnt = 0

    def __init__(self, loca, name, product, cust) :
        self.loca = loca
        self.name = name
        self.product = product
        self.cust = cust
        supermarket.inst_cnt += 1
    
    def print_loca(self) :
        print(f"{self.loca}에 위치해 있습니다.")

    def change_category(self, product) :
        before = self.product
        self.product = product
        print(f"{before} 에서 {self.product} 로 변경되었씀") 
    
    def show_list(self) :
        print(f"{self.print_loca}를 팔고있음")
    
    def enter_cust(self) :
        self.cust += 1

    def show_info(self) :
        print(f":: 슈퍼마켓 정보 ::")
        print(f"{self.name} 이라는 이름을 가짐")
        print(f"{self.loca} 의 위치에 있습니다.")
        print(f"{self.product} 의 상품을 팔아요")
        print(f"{self.cust} 명의 손님이 있어요")
        print(f"{self.inst_cnt} 이게 몇개임?")

test = supermarket("서울", "도깨비상점", "대환단", "7")
test2 = supermarket("종로", "비형상점", "사진", "8")
test3 = supermarket("종각", "전상점", "개연성", "9")

print(test.show_info())

print(supermarket.inst_cnt, "개의 인스턴스가 있습미다 ")