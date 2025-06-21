import collections

def main(N,A):
    B=[0]
    count = 0
    for i in range(N):
        T = A[i] + B[i]

        B.append(T)
    c = collections.Counter(B)

    for i in range(len(c)):
        k, v = c.popitem()
        for z in range(v):
            count += z

    return print(count)

if __name__ == "__main__":
    N=int(input())
    A=list(map(int,input().split()))

    main(N,A)