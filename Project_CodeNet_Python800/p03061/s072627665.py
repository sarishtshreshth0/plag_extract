import math

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 2:
        print(max(A))
        exit()
    l_gcd = [A[0]]
    for a in A[1:N-1]:
        l_gcd.append(math.gcd(l_gcd[-1], a))
    r_gcd = [A[-1]]
    for a in list(reversed(A))[1:N-1]:
        r_gcd.append(math.gcd(r_gcd[-1], a))

    ans = 1
    for i in range(N):
        if i == 0:
            v = r_gcd[-1]
        elif i == N-1:
            v = l_gcd[-1]
        else:
            v = math.gcd(l_gcd[i-1], r_gcd[N-i-2])
        if v > ans:
            ans = v
    print(ans)


if __name__ == '__main__':
    main()
