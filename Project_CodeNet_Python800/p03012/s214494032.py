n = int(input())
apple = list(map(int, input().split()))
a = 100000
for i in range(1, n):
    a = min(a, abs(sum(apple[:i]) - sum(apple[i:])))
print(a)