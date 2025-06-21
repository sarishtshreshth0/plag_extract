a, b = map(int, input().split())
l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
s = input()
flag = True
for i in range(len(s)):
    if i == a:
        if s[i] != '-':
            flag = False
    elif s[i] not in l:
        flag = False
if flag:
    print("Yes")
else:
    print("No")