def main(N,A):
    B=[0]
    count = 0
    for i in range(N):
        T = A[i] + B[i]

        B.append(T)


    B = sorted(B)
    # print(B)
    c = 0
    for i in range(len(B)):
        if i==0:
            continue
        if B[i] == B[i-1]:
            c+=1
            count +=c
            # print(c)
            # 
            # print(count)
        else:
            c = 0

    return print(count)

if __name__ == "__main__":
    N=int(input())
    A=list(map(int,input().split()))

    main(N,A)
