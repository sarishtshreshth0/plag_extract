n = input()
t = ["3","5","7"]
for i in range(8):
    s = []
    for j in t:
        s.append(j+"3")
        s.append(j+"5")
        s.append(j+"7")
    t += s
t = set(t)
t = list(t)
t.sort()
count = 0
for i in range(len(t)):
    if len(t[i]) > len(n):
        continue
    if int(t[i]) > int(n):
        continue
    if '3' in t[i] and '5' in t[i] and '7' in t[i]:
        count+=1
print(count)