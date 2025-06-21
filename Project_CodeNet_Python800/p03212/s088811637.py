N = int(input())
Count = 0
if N>=357:
    Flag = True
    Now = ['33','35','37','53','55','57','73','75','77']
    TFS = ['3','5','7']
    Nex = []
    while int(Now[-1])<=N:
        for TNow in Now:
            for TTFS in TFS:
                Nex.append(TNow+TTFS)  
        for TNex in Nex:
            if all(TNex.count(C)>0 for C in '357') and int(TNex)<=N:
                Count += 1
        Now = Nex
        Nex = []
print(Count)