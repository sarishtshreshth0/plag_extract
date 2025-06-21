N = int(input())
L = list(map(int, input().split()))

MinatoYukina = [0]*100003

for i in range (0, N):
	MinatoYukina[L[i]]+=1
	MinatoYukina[L[i]+1]+=1
	MinatoYukina[L[i]+2]+=1

print(max(MinatoYukina))