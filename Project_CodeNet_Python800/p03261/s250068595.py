n = int(input())
l = [input()]

flag = True

for i in range(n-1):
    s = input()
    if s not in l and s[0] == l[-1][-1]:
        l.append(s)
    else:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")