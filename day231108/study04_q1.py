"""
이름 나이 입력받기. 안녕하세요! 홍길동님! (100세) 출력
이름 년도 올해년도 출력 나이 계산해서 출력하기.
"""

print("Q1 ############")
q1_name = input("이름을 입력하세요. : ")
q1_age = input("나이를 입력하세요 : " )

print("안녕하세요! ", q1_name, "님", " (", q1_age,")", sep="")

print("Q2 ############")
q2_name = input("이름을 입력하세요. : ")
q2_year = input("태어난 년도를 입력하세요 : " )
q2_nowyear = input("올해 년도를 입력하세요 : " )
q2_age = int(q2_nowyear)-int(q2_year)+1

print("올해는 ", q2_nowyear, ", ", q2_name, "님의 나이는 ", q2_age, "세 입니다.", sep="")

