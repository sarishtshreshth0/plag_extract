n = int(input())
AB = [list(map(int, input().split())) for _ in range(n)]
CD = [list(map(int, input().split())) for _ in range(n)]

AB_sorted_y = sorted(AB, key=lambda x: x[1])
CD_sorted_x = sorted(CD, key=lambda x: x[0])

bool_AB = [False] * n
bool_CD = [False] * n

res = 0
for i in range(n):
    c, d = CD_sorted_x[i]
    for j in range(n - 1, -1, -1):
        a, b = AB_sorted_y[j]
        if bool_CD[i] == False and bool_AB[j] == False and a < c and b < d:
            res += 1
            bool_AB[j] = True
            bool_CD[i] = True

print(res)