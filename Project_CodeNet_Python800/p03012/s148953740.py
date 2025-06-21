def main():
    N = int(input())
    w = list(map(int, input().split()))
    record = []
    t = 0
    for i in range(1, N):
        t = t + w[i-1]
        record.append(abs(t - sum(w[i:N])))
    record.sort()
    print(record[0])
main()  