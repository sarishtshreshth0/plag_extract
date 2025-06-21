a, b = map(int, input().split())
flag = 0
for i in range(1,4):
    if a * b * i % 2 != 0:
        flag = 1
        break
if flag == 0:
    print('No')
else:
    print('Yes')