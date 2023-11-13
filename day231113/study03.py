
input_id = input("아이디를 입력하세요.")
input_pw = input("비밀번호")

f = open("./member.txt","r")

for line in f :
    text = line.split()
    login_flag = False

    if text[0] == input_id and text[1] == input_pw :
        login_flag = True
        break
f.close()

if login_flag == True :
    print("로그인 성공")
    te = open("./member_tel.txt","r")

    tel_flag = False # 없는 사람

    for line in te :
        tel_text = line.split()
        tel_flag = False

        if tel_text[0] == input_id and tel_text[1] == input_pw :
            tel_flag = True # 이미 있는 사람 

    te.close()


    if tel_flag == True :
        print("이미 있음 실행")
        tel_ = open("./member_tel.txt", "r")
        lines = tel_.readlines()
        tel_.close()
        tel = input("전화번호 입력")
        # member_tel.txt 파일에서 해당 아이디의 라인을 찾아 전화번호를 수정
        with open("./member_tel.txt", "w") as tel_file:
            for line in lines:
                tel_text = line.split()
                if tel_text[0] == input_id:
                    tel_file.write(f"{input_id} {input_pw} {tel}\n")
                else:
                    tel_file.write(line)

    else : 
        print("없음 실행")
        fel_ = open("./member_tel.txt","a")
        tel = input("전화번호 입력")
        fel_.write(f"\n{input_id} {input_pw} {tel}\n")
        fel_.close()
        
else :
    print("로그인 실패")