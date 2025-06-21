A,B,C,D = map(int, input().split())
a = []
b = []
for i in range(A,B+1):
    a.append(i)
for i in range(C,D+1):
    b.append(i)
print(max(len(set(a)&set(b))-1,0))