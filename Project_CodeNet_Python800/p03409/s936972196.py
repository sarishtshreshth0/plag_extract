casen=0
if casen==0:
    a=[]
    c=[]
    n=int(input())
    for i in range(n):
        ai,bi=map(int,input().split())
        a.append([ai,bi])
    for i in range(n):
        ci,di=map(int,input().split())
        c.append([ci,di])
elif casen==1:
    n=3
    a=[[2,0],[3,1],[1,3]]
    c=[[4,2],[0,4],[5,5]]
elif casen==2:
    n=3
    a=[[0,0],[1,1],[5,2]]
    c=[[2,3],[3,4],[4,5]]
elif casen==3:
    n=2
    a=[[2,2],[3,3]]
    c=[[0,0],[1,1]]
elif casen==4:
    n=5
    a=[[0,0],[7,3],[2,2],[4,8],[1,6]]
    c=[[8,5],[6,9],[5,4],[9,1],[3,7]]
elif casen==5:
    n=5
    a=[[0,0],[1,1],[5,5],[6,6],[7,7]]
    c=[[2,2],[3,3],[4,4],[8,8],[9,9]]

c.sort()
a.sort(key=lambda x:x[1])
#a.reverse()

icnt=0
ic2=0
for ic in range(len(c)):
    for ia in range(len(a)-1,-1,-1):
        if a[ia][0]<c[ic][0] and a[ia][1]<c[ic][1]:
            icnt=icnt+1
            del a[ia]
            break
        else:
            continue
        break

print(icnt)               