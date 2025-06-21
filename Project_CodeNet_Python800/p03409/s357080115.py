def main():
    n = int(input())
    R = [list(map(int,input().split())) for _ in range(n)]
    B = [list(map(int,input().split())) for _ in range(n)]

    R = sorted(R, key=lambda x: x[1], reverse=True)
    B = sorted(B, key=lambda x: x[0])

    used = []
    for i in range(n):
        for j in range(n):
            if (R[j] not in used) and (R[j][0] < B[i][0]) and R[j][1] < B[i][1]:
                used.append(R[j])
                break
    print(len(used))


if __name__ == '__main__':
    main()
