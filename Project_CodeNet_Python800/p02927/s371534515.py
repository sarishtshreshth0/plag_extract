import sys
input = sys.stdin.readline

m, d = map(int, input().split())
ans = 0
for i in range(1, m + 1):
    for j in range(22, d + 1):
        len_1 = int(str(j)[0])
        len_2 = int(str(j)[1])
        if len_1 >= 2 and len_2 >= 2 and len_1 * len_2 == i:
            ans += 1
print(ans)
