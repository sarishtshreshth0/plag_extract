N=int(input())
S=input()

K=0
A="*"
for s in S:
    if s!=A:
        A=s
        K+=1
print(K)