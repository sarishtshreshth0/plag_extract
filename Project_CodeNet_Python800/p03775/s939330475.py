N = int(input())
ans = 10
for i in range(1,10**5+1):
    if N % i == 0:
        A = i
        B = N//i
        stA = str(A)
        stB = str(B)
        ans = min(ans,max(len(stA),len(stB)))
    else:
        pass
print(ans)