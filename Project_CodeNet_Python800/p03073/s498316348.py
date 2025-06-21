S = list(map(int,list(input())))
N = len(S)

sirokuro =[i%2 for i in range(0,N,1)]
kurosiro =[(i+1)%2 for i in range(0,N,1)]

loss1 = 0
for i in range(0,N,1):
    if S[i]!=sirokuro[i]:
        loss1 +=1

loss2 = 0
for i in range(0,N,1):
    if S[i]!=kurosiro[i]:
        loss2+=1

print(min(loss1,loss2))