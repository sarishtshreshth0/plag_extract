N = int(input())
S = list(input())
cn = 1

for i in range(N-1):
    if S[i] == S[i+1]:
        continue
    else:
        cn = cn + 1
        
print(cn)