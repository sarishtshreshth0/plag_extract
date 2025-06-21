s = [i for i in range(2,14)] + [1]
a, b = map(int, input().split())
c=s.index(a)
d=s.index(b)
print('Draw' if c==d else ["Bob","Alice"][c > d])