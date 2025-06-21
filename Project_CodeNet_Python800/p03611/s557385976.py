import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    n = I()
    a = LI()
    max_a = max(a)
    if max_a == 0 or max_a == 1:
        print(len(a))
        sys.exit()
    t = [0]*(max_a+1)
    for i in a:
        t[i] += 1
    ans = 0
    for i in range(1, len(t)-1):
        temp = t[i-1] + t[i] + t[i+1]
        ans = max(ans, temp)
    print(ans)

if __name__ == '__main__':
    main()