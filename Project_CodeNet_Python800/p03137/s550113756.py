n, m, *xx = map(int, open(0).read().split())

xx.sort()

diff = [a - b for a, b in zip(xx[1:], xx[:-1])]

diff.sort(reverse=True)

print(sum(diff[n-1:]))