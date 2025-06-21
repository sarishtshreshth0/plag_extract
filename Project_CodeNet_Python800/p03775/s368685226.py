N = int(input())
maxn = N
for i in range(1,int(N**(1/2))+1):
    # print(i)
    if N%i==0:
        maxn = min(maxn,len(str(N//i)))
        # print(i,N//i)

print(maxn)