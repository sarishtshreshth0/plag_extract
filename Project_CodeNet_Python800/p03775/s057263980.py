N = int(input())
ans = []
b = 0
c = 0
for a in range(1, int(N**0.5) + 1):
    b = N//a
    c = max(len(str(a)),len(str(b)))
    if a*b == N:
        ans.append(c)
print(min(ans))
