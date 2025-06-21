import sys
sys.setrecursionlimit(10 ** 8)

def main():
    N = int(input())

    i = 1
    ans = 15
    while i*i <= N:
        if N%i==0:
            # bのほうが必ず大きくなる
            a = i
            b = N//i
            ans = min(ans,len(str(b)))
        i += 1

    print(ans)
if __name__ == '__main__':
    main()
