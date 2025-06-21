from sys import stdin
M, D = [int(_) for _ in stdin.readline().rstrip().split()]
ans = 0
for i in range(1, M+1):
    for j in range(1, D+1):
        d1 = int(j%10)
        d10 = int(j/10)
        if d1 >= 2 and d10 >= 2 and d1*d10 == i:
            ans += 1
print(ans)
