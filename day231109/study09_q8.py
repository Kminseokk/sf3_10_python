import sys
input = sys.stdin.readline
N, M = map(int, input().split())

DI = dict()
cnt = 0

for i in range(N):
    Nword = input()
    DI[Nword] = True
    
for i in range(M):
    Mword = input()
    if Mword in DI.keys():
        cnt+=1
print(cnt)