n = int(input())
a = input()
s = {a}
a = a[-1]
c = 1
for _ in range(n-1):
    b = input()
    if a == b[0]:
        a = b[-1]
        c += 1
        s.add(b)
    else:
        print('No')
        break
else:
    print('Yes' if len(s) == c else 'No')