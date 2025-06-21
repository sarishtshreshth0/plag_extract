a, b = map(int,input().split())
cnt = 0

for i in range(1,4):
    if a*b*i % 2 != 0:
        cnt += 1

if cnt >= 1:
    print('Yes')
else:
    print('No')