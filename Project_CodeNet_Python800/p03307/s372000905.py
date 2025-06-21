import fractions

def main():
    n = int(input())
    print(int(2*n/fractions.gcd(2, n)))


if __name__ == '__main__':
    main()
