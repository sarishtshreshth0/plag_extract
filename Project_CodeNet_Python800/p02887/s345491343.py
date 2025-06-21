N=int(input())
S=input()
K=S
i=0
han=S[0]
kot=S[0]

for b in K:
    if b != han:
        kot+=b
        han=b



print(len(kot))