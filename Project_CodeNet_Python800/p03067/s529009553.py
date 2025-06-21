from sys import stdin


def main():
    A, B, C = [int(x) for x in stdin.readline().rstrip().split()]
    print('Yes' if (A <= C <= B) or (B <= C <= A) else 'No')


if __name__ == "__main__":
    main()
