n=int(input())
a=list(map(int,input().split()))
a.sort()
i=0
ans=0
while i < n:
    k=i
    index=i
    while a[k]-a[i]<= 2:
        k += 1
        if k == n:
            break
    while a[index] == a[i]:
        index += 1
        if index == n:
            break
    ans=max(k-i,ans)
    if index == n:
        break
    i=index
print(ans)