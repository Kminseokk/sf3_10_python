
input_id = input("아이디를 입력하세요.")
input_pw = input("비밀번호")

f = open("./member.txt","r")

for line in f :
    text = line.split()
    login_flag = False

    if text[0] == input_id and text[1] == input_pw :
        login_flag = True
        break

if login_flag == True :
    print("로그인 성공")
else :
    print("로그인 실패")
