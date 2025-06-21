A,B,C,D=map(int,input().split())
Ans = [0] * 101
for i in range(100+1):
    if A<=i and i<B:
        Ans[i]+=1
    if C<=i and i<D:
        Ans[i]+=1

print(Ans.count(2))
