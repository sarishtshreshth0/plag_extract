s = list(input())
a = 0
b = 0
f = 0
for i in s:
    if f == 0:
        if i == "0":
            a += 1
        else:
            b += 1
        f = 1
    else:
        if i == "0":
            b += 1
        else:
            a += 1
        f = 0
            
print(min(a,b))