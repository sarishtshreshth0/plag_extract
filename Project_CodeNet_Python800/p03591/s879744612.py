S = input()
flag = 0
k = "YAKI"
if len(S)<4:
    print("No")
    flag = 1
else:
    for i in range(4):
        if S[i] != k[i]:
            flag = 1
            print("No")
            break
if flag == 0:
    print("Yes")