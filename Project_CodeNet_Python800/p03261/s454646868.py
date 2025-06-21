#b
N=int(input())
W=[None]*N
for i in range(N):
    W[i] = input()


if all( W[i][0]==W[i-1][-1] for i in range(1,N) ) and len(set(W))==N:
    print("Yes")
else:
    print("No")