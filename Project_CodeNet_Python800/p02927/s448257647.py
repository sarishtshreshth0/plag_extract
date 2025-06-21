from sys import exit, stderr, stdin
input = stdin.readline
# setrecursionlimit(10**7)

def debug(var, name="hoge"):
    print(name +":" + str(type(var)) + " = " + repr(var), file=stderr)
    return


def main():
    M, D = [int(n) for n in input().split()]
    ans = 0
    for i in range(2,10):
        for j in range(2,10):
            for m in range(1,M+1):
                if i*10 + j <= D and i*j == m:
                    ans += 1
    print(ans)



if __name__ == "__main__":
    main()
