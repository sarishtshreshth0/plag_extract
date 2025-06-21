n = int(input())
data = list(map(int, input().split()))

def gcd(a, b):
    while b:
        a, b = b, a % b
        # print("a b", a, b)
    return a

left_ = [0] * (n + 1)
right_ = [0] * (n + 1)
ans = []

for i in range(n):
    left_[i] = gcd( left_[i-1], data[i] )

for i in range(n-1, 0, -1):
    right_[i] = gcd( right_[i+1], data[i] )

for i in range(n):
    ans += [ gcd( left_[i-1], right_[i+1] ) ]

print( max(ans) )
