# https://atcoder.jp/contests/abc091/tasks/arc092_a
n = int(input())
coordinates_red = [list(map(int, input().split())) for _ in range(n)]
coordinates_blue = [list(map(int, input().split())) for _ in range(n)]
coordinates_red.sort()
coordinates_blue.sort()
#print(coordinates_red)
#print(coordinates_blue)

start = 0
ans = 0
for blue in coordinates_blue:
    candidate = []
    for red in coordinates_red:
        #print(blue)
        #print(red)
        if red[0] < blue[0] and red[1] < blue[1]:
            candidate.append(red)
    if candidate:
        candidate.sort(key=lambda x: x[1])
        coordinates_red.remove(candidate.pop(-1))
        ans += 1

print(ans)