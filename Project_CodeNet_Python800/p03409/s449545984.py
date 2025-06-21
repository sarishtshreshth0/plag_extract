N=int(input())
AB=sorted([list(map(int,input().split())) for _ in range(N)])
CD=sorted([list(map(int,input().split())) for _ in range(N)], key=lambda x:x[1])

cnt=0
for a,b in AB[::-1]:
    for i,j in enumerate(CD):
        c,d=j
        if a<c and b<d:
            cnt +=1
            del CD[i]
            break
print(cnt)