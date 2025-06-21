n = int(input())
w = list(map(int,input().split()))

total = sum(w)
s2 = total
minimum = total
for i in range(1,n):
    s2 -= w[i-1]
    minimum = min(minimum,abs(total-s2*2))
print(minimum)
