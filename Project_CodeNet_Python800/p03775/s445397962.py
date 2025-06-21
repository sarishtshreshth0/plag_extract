n = int(input())
a = []
for i in range(1,int(n**(0.5))+1):
    if n%i == 0:
        a.append(i)
m = max(a)
c = int(n/m)
keta = len(str(c))
print(keta)