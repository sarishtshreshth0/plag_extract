N = int(input())

Cost = [0]
Start = [0]
Frequency = [0]
Ans = [0] * (N+1)

for __ in range(N-1):
    c, s, f = map(int, input().split())
    Cost.append(c)
    Start.append(s)
    Frequency.append(f)

for i in range(1, N):
    if Ans[i] != 0:
        print(Ans[i])
    else:
        Same = []
        now = 0
        for j in range(i, N):
            if now <= Start[j]:
                if Ans[j] != 0:
                    now = Ans[j]
                    break
                Same.append(j)
                now = Start[j] + Cost[j]
            else:
                tmp = (now-1) // Frequency[j]
                tim = (tmp + 1) * Frequency[j]
                now = tim + Cost[j]
        print(now)
        for k in Same:
            Ans[k] = now
print(0)

