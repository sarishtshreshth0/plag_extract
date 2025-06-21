n = int(input())
w = list(map(int, input().split()))
l = []
for i in range(n):
    s1 = sum(w[i:])
    s2 = sum(w[:i])
    l.append(abs(s1- s2))
print(min(l))