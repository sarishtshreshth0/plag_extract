n = int(input())
a = list(map(int, input().split()))
di = {0:1}
accu = 0
for i in a:
    accu += i
    if accu in di:
        di[accu] += 1
    else:
        di[accu] = 1
ans = 0
for i in di.values():
    ans += i*(i-1)//2
print(ans)