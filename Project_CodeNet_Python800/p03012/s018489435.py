N = int(input())
W = list(map(int, input().split()))
b = 0
a = sum(W)
diff = abs(b-a)
for i in range(N):
    b += W[i]
    a -= W[i]
    diff = min(diff,abs(b-a))
print(diff)