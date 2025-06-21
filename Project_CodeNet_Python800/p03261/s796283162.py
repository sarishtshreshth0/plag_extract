def main():
    N = int(input())
    A = [input()]
    for i in range(1, N):
        W = input()
        if A[-1][-1] == W[0]:
            for j in range(i):
                if A[j] == W:
                    print("No")
                    return
            A.append(W)
        else:
            print("No")
            return
    print("Yes")

main()