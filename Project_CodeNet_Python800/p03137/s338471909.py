import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n, m = map(int, input().split())
    x = sorted(list(map(int, input().split())))
    diff = []
    for i in range(1, m):
        diff.append(x[i]-x[i-1])
    diff.sort(reverse=True)
    print(x[-1]-x[0]-sum(diff[:n-1]))
        
if __name__ == '__main__':
    main()