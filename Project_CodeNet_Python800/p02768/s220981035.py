n,a,b = map(int,input().split())
m = 10**9 + 7
comb_a = 1
comb_b = 1

a_num = list(range(1,a+1))
j = 0
for i in range(1,a+1):
    comb_a *= (n-i+1)
    comb_a *= pow(a_num[i-1],m-2,m)
    comb_a = comb_a % m

b_num = list(range(1,b+1))
j = 0
for i in range(1,b+1):
    comb_b *= (n-i+1)
    comb_b *= pow(b_num[i-1],m-2,m)
    comb_b = comb_b % m

ans = pow(2,n,m) - comb_a - comb_b - 1
print(int(ans) % m)