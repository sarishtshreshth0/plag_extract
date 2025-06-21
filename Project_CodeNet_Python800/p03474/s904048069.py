a,b=map(int,input().split())
s=input()
li=[str(i) for i in range(10)]
res="Yes"
if s[a]!="-":
    res="No"
for i in range(0,a):
    if s[i] not in li:
        res="No"
for j in range(a+1,a+b+1):
    if s[j] not in li:
        res="No"
print(res)
