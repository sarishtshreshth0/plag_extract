n = int(input())
before = ''
said = set([])
f = True
for i in range(n):
    if i==0:
        before = input()
        said.add(before)
        continue
    s = input()
    if before[-1] != s[0] or s in said:
        f = False
    before = s
    said.add(s)
print('Yes' if f else 'No')

