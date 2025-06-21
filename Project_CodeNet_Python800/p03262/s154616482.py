def main():
    import math
    import functools
    n, x = map(int, input().split())
    inset = set(map(int, input().split()))
    inset2 = set()

    for num in inset:
        inset2.add(abs(num - x))

    gcd = functools.reduce(math.gcd, inset2)
    print(gcd)

            



if __name__ == "__main__":
    main()