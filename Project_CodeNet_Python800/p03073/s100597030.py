li = list(input())
l = [int(n) for n in li]
x = len(l)
li_0 = [0 for i in range(x)]
li_1 = [0 for i in range(x)]
for i in range(x):
    if i % 2 == 0:
        li_0[i] = 1
    else:
        li_1[1] = 1
a = 0
b = 0
for i in range(x):
    if li_0[i] != l[i]:
        a += 1
    else:
        b += 1
print(min(a,b))