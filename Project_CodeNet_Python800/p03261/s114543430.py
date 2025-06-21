n = int(input())
w = [input() for i in range(n)]
a = []
a.append(w[0])
now = w[0]
ans = True
for i in w[1:]:
    if i not in a and now[-1] == i[0]:
        now = i
        a.append(i)
    else:
        ans = False
        break
if ans:
    print("Yes")
else:
    print("No")