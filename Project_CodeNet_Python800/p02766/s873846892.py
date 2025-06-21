
def main():
    N, K = map(int, input().split())
    ans = base10to(N, K)
    print(len(ans))

def base10to(n, b):
    if (int(n/b)):
       return base10to(int(n/b), b) + str(n%b)
    return str(n%b)

if __name__ == '__main__':
    main()
