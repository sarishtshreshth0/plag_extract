a, b, c, d = list(map(int, input().split()))
def overlap(a, b):
    if max(a[0], b[0]) > min(a[1], b[1]):
        return [0, 0]
    return [max(a[0], b[0]), min(a[1], b[1])]
ans = overlap([a, b], [c, d])
print(ans[1] - ans[0])