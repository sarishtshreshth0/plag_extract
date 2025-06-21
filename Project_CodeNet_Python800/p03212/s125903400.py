n = int(input())

def Base_10_to_n(X, n=3):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

s = 0
m = 0

f = len(str(n))

for i in range(1, f):
    if i < 3:
        pass
    else:
        s += 3 ** i - 3 * (2 ** i) + 3 

while True:
    l = Base_10_to_n(m)
    flag = [False] * 3
    if len(l) < f:
        l = "0" * (f-len(l)) + l
    k = ""
    for i in range(len(l)):
        if l[i] == "0":
            k += "3"
            flag[0] = True
        elif l[i] == "1":
            k += "5"
            flag[1] = True
        else:
            k += "7"
            flag[2] = True
    #print(k)

    if int(k) <= n:
        if False not in flag:
            s += 1
        m += 1
    else:
        break

print(s)