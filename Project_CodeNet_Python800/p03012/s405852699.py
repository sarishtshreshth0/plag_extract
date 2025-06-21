n = int(input())
w = list(map(int, input().split()))
t = 10**9
for i in range(1,n):
    s1 = sum(w[:i])
    s2 = sum(w[i:])
    if abs(s1-s2) < t:
        t = abs(s1-s2)
print(t)