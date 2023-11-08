
rainbow = ['red','ora','yell','green','blue','indi','pur']

print("2번 인덱스 값 :", rainbow[2])

rainbow.sort()
print("알파벳 순서로 정렬 :", rainbow)

rainbow.append("white")
print("좋아하는 색 마지막에 추가 :", rainbow)

del rainbow[3:6]
print("3~6번째 값 삭제 :", rainbow)