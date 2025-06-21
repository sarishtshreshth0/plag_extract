s = input()

txt = "YAKI"

for i in range(4):
    if(len(s) < 4):
        flag = 0
        break
    if(s[i] == txt[i]):
        flag = 1
    else:
        flag = 0
        break

if(flag == 1):
    print("Yes")
else:
    print("No")