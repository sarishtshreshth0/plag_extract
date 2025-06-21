n = int(input())
w = []
for i in range(n):
    tmp = input()
    w.append(tmp)

ans = True
for i in range(1, n):
    if w[i][0] != w[i-1][len(w[i-1])-1]:
        ans = False
        break
    else:
        for j in range(0, i):
            if w[j] == w[i]:
                ans = False
                break

if ans:
    print("Yes")
else:
    print("No")