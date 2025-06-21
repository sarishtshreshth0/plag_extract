import collections
N = int(input())
Num,Count = zip(*sorted(collections.Counter(int(T) for T in input().split()).most_common()))
DisN = ((min(Num)-1),)+Num+((max(Num)+1),)
DisC = (0,)+Count+(0,)
MAX = 0
for T in range(1,len(Num)+1):
    Dis = DisC[T]
    if DisN[T-1]==DisN[T]-1:
        Dis += DisC[T-1]
    if DisN[T+1]==DisN[T]+1:
        Dis += DisC[T+1]
    if MAX<Dis:
        MAX = Dis
print(MAX)