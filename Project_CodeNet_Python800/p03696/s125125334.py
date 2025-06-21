N = int(input())
S = list(input())
d = []

for i in range(N+1):
    partial = S[:i]
    d.append(partial.count('(') - partial.count(')'))

a = -min(d)
b = d[-1]

print('(' * a + "".join(S) + ')' * (b + a))