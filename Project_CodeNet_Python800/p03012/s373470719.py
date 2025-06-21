n = int(input())
w = list(map(int, input().split()))
l = [abs(sum(w[:i]) - sum(w[i:])) for i in range(1, n)]
print(min(l))