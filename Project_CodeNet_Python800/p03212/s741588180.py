from itertools import product
N = int(input())
STR_N = str(N)
all_pat =[]
for i in range(3,len(STR_N)+1):
    pattern = list(product(["7","5","3"],repeat=i))
    for p in pattern:
        if len(set(p))==3:
            all_pat.append(int(''.join(p)))
all_pat = list(set(all_pat))
all_pat.sort()
cnt = 0
for a in all_pat:
    if a<=N:
        cnt+=1
print(cnt)