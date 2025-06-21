def f(a, b):
    return len(str(max(a, b)))
def main():
    n = int(input())
    ans = 100
    for i in range(1, int(n ** 0.5 + 0.5) + 1):
        if n % i == 0:
            ans = min(ans, f(i, n // i))
    print(ans)

if __name__ == '__main__':
    main()
