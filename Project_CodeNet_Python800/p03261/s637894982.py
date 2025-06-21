N = int(input())
L = [str(input()) for i in range(N)]
flag = 1

for i in range(N):
    if L.count(str(L[i]))<2:
        if str(L[i-1])[-1] == str(L[i])[0]:
            pass
        elif i == 0:
            pass
        else:
            flag = 0
    else:
        flag = 0

if flag:
    print("Yes")

else:
    print("No")
