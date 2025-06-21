n = input()

d = {3: 0b001, 5: 0b010, 7: 0b100}

dp = [[[0] * 2 for _ in range(1 << 3)] for _ in range(len(n) + 1)]
dp[0][0][1] = 1

for i, e in enumerate(n):
    e = int(e)
    for num in [0, 3, 5, 7]:
        if num == 0:
            dp[i+1][0b000][0] += sum(dp[i][0b000])
            continue
        for j in range(1 << 3):
            if num == e:
                dp[i+1][j|d[num]][1] += dp[i][j][1]

            elif num < e:
                dp[i+1][j|d[num]][0] += dp[i][j][1]

            dp[i+1][j|d[num]][0] += dp[i][j][0]

ans = sum(dp[len(n)][0b111])
print(ans)
