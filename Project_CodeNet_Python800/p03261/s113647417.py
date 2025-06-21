n=int(input())
tmp=input()
t=tmp[-1]
s=set()
s.add(tmp)
for i in range(n-1):
    tmp=input()
    if tmp[0]!=t:
        print("No")
        exit()
    if tmp in s:
        print("No")
        exit()
    s.add(tmp)
    t=tmp[-1]
print("Yes")
