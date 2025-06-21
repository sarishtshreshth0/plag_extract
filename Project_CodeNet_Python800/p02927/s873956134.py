M,D=map(int,input().split())
cnt=0
for i in range(1,M+1):
    for j in range(1,D+1):
        iti=j%10
        ju=j//10
        if iti>=2 and ju>=2 and i==iti*ju:
            cnt+=1

print(cnt)
