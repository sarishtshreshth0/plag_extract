def main(N, A, B ,S):
    status = [None for _ in range(N)]
    c_all, c_for = 0, 0
    for i, s in enumerate(S):
        if s == 'a' and c_all < A + B:
            c_all += 1
            status[i] = 'Yes'
        elif s == 'b' and c_all < A + B and c_for < B:
            c_all += 1
            c_for += 1
            status[i] = 'Yes'
        else:
            status[i] = 'No'
    return status


if __name__ == "__main__":
    N, A, B = map(int, input().split())
    S = input()
    ans = main(N, A, B, S)
    for i in ans:
        print(i)
