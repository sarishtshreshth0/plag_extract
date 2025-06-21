def f(a, b):
    return max(len(str(a)), len(str(b)))

import math
def main():
    N = int(input())

    ans = 10**10
    for i in range(1, int(math.sqrt(N)) + 1):
        j = N // i

        if i * j == N:
            ans = min(ans, f(i, j))

    print(ans)

if __name__ == "__main__":
    main()