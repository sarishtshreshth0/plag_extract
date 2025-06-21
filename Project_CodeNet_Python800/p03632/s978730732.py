a,b,c,d = map(int, input().split())
alice = list(range(a,b+1))
bob = list(range(c,d+1))
ab = alice + bob
l= [i for i in set(ab) if ab.count(i) > 1]
if 0 == len(l) or 1 == len(l):
    print(0)
elif 2 == len(l):
    print(1)
else:
    print(max(l) - min(l))