n=int(input())
w=[str(input())]
ans="Yes"
for i in range(n-1):
    x=str(input())
    if x in w:
        ans="No"
        break
    w.append(x)
    y=w[i]
    if x[0]!=y[-1]:
        ans="No"
        break
print(ans)