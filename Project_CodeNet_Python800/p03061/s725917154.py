n = int(input())
a = list(map(int,input().split()))

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

left_gcd = [0]*(n+1)
right_gcd = [0]*(n+1)
left_gcd[1] = a[0]
right_gcd[1] = a[-1]

for i in range(1,n):
    left_gcd[i+1] = gcd(left_gcd[i],a[i])
    right_gcd[i+1] = gcd(right_gcd[i],a[-1-i])

ans = right_gcd[n-1]
for i in range(n):
    ans = max(ans,gcd(left_gcd[i],right_gcd[n-1-i]))
print(ans)
