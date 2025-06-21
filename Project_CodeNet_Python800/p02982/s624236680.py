def good_distance():
    N, D = input().split()
    N = int(N)
    D = int(D)
    P = list()
    for a in range(N):
        P.append(list())
        P[a] = input().split()
    for a in range(N):
        for b in range(D):
            P[a][b] = int(P[a][b])
    print()
    result = cal_good_distance(P, D)
    print(result)

def cal_good_distance(x, D):
    count = 0
    count_a = 0
    for a in x:
        if count_a == len(x):
            break
        for b in range(count_a+1, len(x)):
            distance = 0
            for i in range(D):
                distance = distance + (x[count_a][i] - x[b][i])**2
            distance = distance ** (1/2)
            try:
                if isinstance(distance, int) or distance.is_integer():
                    count += 1
            except AttributeError:
                pass
        count_a += 1
    return count

good_distance()