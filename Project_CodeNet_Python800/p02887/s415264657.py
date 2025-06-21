N=int(input())
S=list(input())

a=0#色変化
for i in range(N-1):
    if not S[i]==S[i+1]:
        a=a+1
print(a+1)