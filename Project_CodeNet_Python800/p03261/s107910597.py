n = int(input())
apple = []
count = 0
for _ in range(n):
    apple.append(str(input()))
for i in range(1,n):
    if apple[i-1][-1] == apple[i][0] and apple[i-1] not in apple[i:]:
        pass
    else:
        count = 1
        break
if apple[-1] not in apple[:-1] and count == 0 and apple[-2][-1]==apple[-1][0]:
    print("Yes")
else:
    print("No")