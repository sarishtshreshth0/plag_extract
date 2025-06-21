import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    A, B = map(int, readline().split())
    if A%2==0 and B%2==0:
        count_1 = (B-A)//2
        ans = (count_1%2)^B
    elif A%2==0 and B%2==1:
        count_1 = (B-A+1)//2
        ans = count_1%2
    elif A%2==1 and B%2==0:
        count_1 = (B-A-1)//2
        ans = A^B^(count_1%2)
    else:
        count_1 = (B-A)//2
        ans = A^(count_1%2)
    print(ans)

if __name__ == '__main__':
    main()