n = int(input())
li = []
ans = True
for i in range(n):
    w = input()
    if len(li) == 0:
        li.append(w)
    else:
        if w in li or w[0] != li[-1][-1]:
            ans = False
        li.append(w)
print("Yes" if ans else "No")
