
N = int(input())
ab = [list(map(int, input().split())) for _ in range(N)]
cd = [list(map(int, input().split())) for _ in range(N)]

ab_sorted = sorted(ab, key = lambda x:x[0], reverse = True)
cd_sorted = sorted(cd, key = lambda x:x[0], reverse = True)


for i in range(len(ab_sorted)):
    candidate = -10e+10
    minimum_size = 10e+10
    for j in range(len(cd_sorted)):
        if cd_sorted[j][0] > ab_sorted[i][0] and cd_sorted[j][1] > ab_sorted[i][1] and minimum_size > cd_sorted[j][1]:
            candidate = j
            minimum_size = cd_sorted[j][1]
    if candidate != -10e+10:
        del cd_sorted[candidate]
print(len(ab_sorted) - len(cd_sorted))