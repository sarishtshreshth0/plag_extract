N=int(input())
S=input()

cs=0
mincs=1000
enc={'(':1,')':-1}

for c in S:
    cs+=enc[c]
    mincs=min(mincs,cs)

while mincs<0:
    S='('+S
    mincs+=1
    cs+=1

while cs>0:
    S=S+')'
    cs-=1

print(S)
