N = int(input())
ls = []
ans = ('Yes')
for i in range(N):
    ls.append(input())
for i in range(1,N):
    if ls[i] in ls[:i]:
        ans = ('No')
        break
    else:
        if ls[i][0] == ls[i-1][-1]:
            continue
        else:
            ans = ('No')
            break
print(ans)