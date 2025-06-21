def Divisor(N):
    Left,RightRev = [],[]
    I = 1
    while I*I<=N:
        if N%I==0:
            Left.append(I)
            if I!=N//I:
                RightRev.append(N//I)
        I += 1
    Div = Left+RightRev[::-1]
    DivCount = len(Div)
    return Div,DivCount
  
N = int(input())
Div,_ = Divisor(N)
FABMax = len(str(N))
for A in Div:
    B = N//A
    if A>B:
        break
    FABMax = min(FABMax,max(len(str(A)),len(str(B))))
print(FABMax)