M, D = map(int, input().split())

ans = 0
if M == 1 or D < 20:
    print(0)
    quit()

for i in range(2, M+1):
    for j in range(21 , D+1):
        if i == (j // 10) * (j % 10) and j % 10 > 1:
            ans += 1
print(ans)