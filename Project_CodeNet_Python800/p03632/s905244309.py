a, b, c , d = map(int, input().split(" "))
start = max(a, c)
end = min(b, d)

diff = end - start
if not diff >= 0:
    diff = 0
print(diff)
