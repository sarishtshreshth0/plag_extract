n = int(input())
csf = [list(map(int,input().split())) for i in range(n - 1)]
#(c, s, f) = i→i+1へc秒かかる。s秒後に発車し、その後はf秒おきに発車する

ans = [0] * n
for i in range(n - 1):
    temp_time = 0
    for j in range(i, n - 1):
        c, s, f = csf[j]
        if temp_time <= s:
            temp_time += s - temp_time + c

        else:
            temp = temp_time % f
            temp_time += (f - temp) % f + c
    ans[i] = temp_time
print(*ans, sep='\n')