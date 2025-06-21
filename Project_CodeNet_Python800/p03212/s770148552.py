c = [0, 3, 5, 7]


N = input()
l = len(N)
N = int(N)


def parse_to_tri(x):
    ret = 0
    d = 1
    for i in range(l):
        ret += c[x % 4]*d
        d *= 10
        x //= 4
    return ret


ans = 0


for i in range(4**l):
    x = parse_to_tri(i)
    s = str(x)
    if '3' not in s or '5' not in s or '7' not in s:
        continue
    if '0' in s:
        continue
    if x <= N:
        ans += 1
print(ans)
