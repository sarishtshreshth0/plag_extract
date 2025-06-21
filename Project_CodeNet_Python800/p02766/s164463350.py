#B
N, K = map(int,input().split())
num=[]
while N >= K:
    num.append(N%K)
    N=N//K
num.append(N)
print(len(num))