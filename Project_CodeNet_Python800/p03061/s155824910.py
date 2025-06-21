import math
N = int(input())
arr = list(map(int, input().split()))
gcd_right = [arr[0]]
for i in range(1,N-1):
    gcd_right.append(math.gcd(gcd_right[i-1],arr[i]))
arr = arr[::-1]
gcd_left = [arr[0]]
for i in range(1,N-1):
    gcd_left.append(math.gcd(gcd_left[i-1],arr[i]))
gcd_left = gcd_left[::-1]
ans = max(gcd_right[-1],gcd_left[0])
for i in range(N-2):
    ans = max(ans,math.gcd(gcd_left[i+1],gcd_right[i]))
print(ans)