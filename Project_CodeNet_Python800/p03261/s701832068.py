n = int(input())
w = [input() for i in range(n)]
for i in range(n):
    flag = True
    for j in range(i):
        if w[i] == w[j]:
            flag = False
    if not flag:
        break
    elif i >= 1 and w[i-1][-1] != w[i][0]:
        flag = False
        break
if flag:
    print("Yes")
else:
    print("No")