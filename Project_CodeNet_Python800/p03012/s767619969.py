N = int(input())
ls1 = list(map(int, input().split()))

a=0
al1=sum(ls1)
b=al1

for i in range(len(ls1)):
    c1=abs(a-b)
    a=sum(ls1[:i+1])
    b=al1-a
    c2=abs(a-b)
    if c1<c2:
        print(c1)
        break
