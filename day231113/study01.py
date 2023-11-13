
f = open("./member.txt","w")

max_user = 3

for i in range(max_user) :
    n, m = input("이름ㅡ 비번 입력").split()
    f.write(f"{n} {m}\n")
f.close()

f = open("./member.txt","r")
print(f.read())
f.close()
