'''A - Multiple of 2 and N
https://atcoder.jp/contests/abc102/tasks/abc102_a

>>> main(3)
6
>>> main(10)
10
>>> main(999999999)
1999999998'''


def main(n):
    if n % 2 == 0:
        print(n)
    else:
        print(n*2)


if __name__ == "__main__":
    n = int(input())

    main(n)
