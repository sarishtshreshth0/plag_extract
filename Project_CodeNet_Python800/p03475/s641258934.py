n = int(input())
c = []
s = []
f = []
for i in range(n - 1):
    ci, si, fi = map(int, input().split())
    c.append(ci)
    s.append(si)
    f.append(fi)
#c, s, f
for i in range(n - 1):
    time = s[i] + c[i]
    for j in range(i + 1, n - 1):
        if time < s[j]:
            time = s[j] + c[j]
        elif time % f[j] != 0:
            time += f[j] - time % f[j] + c[j]
        else:
            time += c[j]
    print(time)
print(0)