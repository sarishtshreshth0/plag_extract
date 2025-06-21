a,b = map(int,input().split())
kazu = [a+i for i in range(4 - a%4)]
kazu.extend([b-i for i in range(b%4+1)])
ans = kazu[0]
for i in range(1,len(kazu)):
    ans = ans ^ kazu[i]
print(ans)