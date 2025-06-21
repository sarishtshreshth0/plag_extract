m, d = map(int, input().split())

cnt = 0

for i in range(10,d+1):
    i1 = i%10
    i10 = i//10
    if i1*i10 <= m and i1 >= 2 and i10 >= 2:
        cnt += 1

print(cnt) 