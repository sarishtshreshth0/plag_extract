import math

def main():
    N, D = map(int, input().split())
    x = []
    for i in range(N):
        x.append(list(map(int, input().split())))
    count = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            t = 0
            for k in range(D):
                t = t + ((x[i][k] - x[j][k]) ** 2)
            t = math.sqrt(t)
            if t.is_integer() == True:
                count += 1
    print(count)
main()  