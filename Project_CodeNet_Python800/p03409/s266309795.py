n=int(input())
red=[tuple(map(int,input().split())) for _ in range(n)]
blue=[tuple(map(int,input().split())) for _ in range(n)]

from operator import itemgetter

red=sorted(red,key=itemgetter(1))
blue=sorted(blue,key=itemgetter(0))
red=red[::-1]
#print(red)
#print(blue)
seen=[0]*n
ans=0
for i in range(n):#blue
    for j in range(n):#red
        if seen[j]==0 and red[j][0]<blue[i][0] and red[j][1]<blue[i][1]:
            seen[j]=1
            ans+=1
            break

print(ans)
