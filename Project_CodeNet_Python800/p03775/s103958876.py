def PrimeDecomp(N,ConcFlag):
    if ConcFlag:
        if N<=1:
            return [1],1
        else:
            I = 2
            PrimeDec = []
            DivCount = 1
            while I*I<=N:
                Cnt = 0
                while N%I==0:
                    N //= I
                    PrimeDec.append(I)
                if Cnt>=1:
                    DivCount *= (Cnt+1)
                I += 1
            if N>=2:
                PrimeDec.append(N)
                DivCount *= 2
            return PrimeDec,DivCount        
    else:
        if N<=1:
            return [1],[1],1
        else:
            I = 2
            PrimeDec = []
            PrimeCnt = []
            DivCount = 1
            while I*I<=N:
                Cnt = 0
                while N%I==0:
                    N //= I
                    Cnt += 1
                if Cnt>=1:
                    PrimeDec.append(I)
                    PrimeCnt.append(Cnt)
                    DivCount *= (Cnt+1)
                I += 1
            if N>=2:
                PrimeDec.append(N)
                PrimeCnt.append(1)
                DivCount *= 2
            return PrimeDec,PrimeCnt,DivCount
          
from itertools import combinations
from operator import mul
from functools import reduce
N = int(input())
PrimeDec,_ = PrimeDecomp(N,True)
FABMax = len(str(N))
for TR in range(1,len(PrimeDec)+1):
    for A in set(reduce(mul,T) for T in combinations(PrimeDec,TR)):
        B = N//A
        FABMax = min(FABMax,max(len(str(A)),len(str(B))))
print(FABMax)