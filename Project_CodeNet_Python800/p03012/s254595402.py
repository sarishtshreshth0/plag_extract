n = int(input())
w = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(abs(sum(w[i:]) - sum(w[:i])))
print(min(a))