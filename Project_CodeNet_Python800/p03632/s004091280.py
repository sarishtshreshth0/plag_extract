A,B,C,D = map(int,input().split())

if A>=D or C>=B:
    print(0)
else:
    li1 = [B,D]
    li2 = [A,C]
    print(min(li1)-max(li2))