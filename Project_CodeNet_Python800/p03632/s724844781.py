a, b, c, d = map(int, input().split())
alice = list(range(a, b))
bob = list(range(c, d))
l = alice + bob
s = set(alice + bob)
print(len(l) - len(s))