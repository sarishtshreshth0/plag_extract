#D
n,a,b = map(int,input().split())

MOD = 10**9 + 7

ans = pow(2,n,MOD) - 1

#n本からa本を選ぶ→繰り返し二乗法
x = 1
#x=n*(n-1)*...*(n-a+1)
for i in range(n-a+1, n+1):
    x *= i
    x %= MOD
#y=a*(a-1)*...*1
for j in range(1,a+1):
    x *= pow(j,MOD-2,MOD)
    x %= MOD
y = 1
#n本からb本選ぶ(aの時と同じ)
for i in range(n-b+1, n+1):
    y *= i
    y %= MOD
#y=a*(a-1)*...*1
for j in range(1,b+1):
    y *= pow(j,MOD-2,MOD)
    y %= MOD
    
ans -= x + y
ans %= MOD
print(ans)