A,B,C,D=map(int,input().split())
cnt=0
for i in range(max(A,B,C,D)):
    if  A<=i<B and C<=i<D:
        cnt+=1
print(cnt)