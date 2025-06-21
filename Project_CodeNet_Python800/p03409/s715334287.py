n = int(input())
r=[list(map(int, input().split())) for i in range(n)]
b=[list(map(int, input().split())) for i in range(n)]
b.sort(key=lambda x:x[0])
p=[]
r_used=[0]*n
for i in range(n):
    q=[]
    for j in range(n):
        if r[j][0]<b[i][0] and r[j][1]<b[i][1]:
            q.append([r[j][1],j])
    q.sort(key=lambda x:x[0],reverse=True)
    p.append(q)
ans = 0
for i in range(n):
    for j in range(len(p[i])):
        if p[i][j][0]<b[i][1] and r_used[p[i][j][1]]==0:
            ans+=1
            r_used[p[i][j][1]]=1
            break
print(ans)
