def calc_digits(n):
    cnt = 0
    while n > 0:
        n //= 10
        cnt += 1
    
    return cnt


N = int(input())

ans = 10**11
for i in range(1,int(N**0.5)+1):
    if N%i == 0:
        B = N//i
        
        tmp = max(calc_digits(i),calc_digits(B))
        
        ans = min(ans,tmp)

print(ans)