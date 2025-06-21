n = int(input())
(*w,) = map(int, input().split())
print(min(abs(sum(w[:i]) - sum(w[i:])) for i in range(1, n)))