N = int(input())

lis = [""]
ans = "Yes"
for i in range(1,N+1):
    W = input()
    if i == 1:
        pass
    else:
        if ((W in lis) == False) and (W[0] == lis[i-1][-1]):
            pass
        else:
            ans = "No"
    lis.append(W)

print(ans)