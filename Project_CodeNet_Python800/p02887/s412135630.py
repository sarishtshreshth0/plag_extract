N=int(input())
S=input()
l=[]
for i in range(N-1):
    if S[i]!=S[i+1]:
        l.append(S[i])
l.append(S[N-1])
print(len(l))