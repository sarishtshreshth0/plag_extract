S = list(input())


L = []
M = []

for i in range(len(S)//2):
    L.append("0")
    L.append("1")
    M.append("1")
    M.append("0")

if (len(S)) % 2 != 0:
    
    L.append("0")
    M.append("1")
    

cn_1 = 0
cn_2 = 0

for i in range(len(S)):
    if S[i] != L[i]:
        cn_1 = cn_1 + 1
    else:
        cn_2 = cn_2 + 1
        
print(min(cn_1, cn_2))