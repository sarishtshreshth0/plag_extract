N = int(input())
ans = len(list(str(N)))
for i in range(1,int(N**(1/2)//1)+1):
    if N%i==0:
        a = i
        b = N//i
        ans = min(ans, max(len(list(str(a))), len(list(str(b)))))
print(ans)