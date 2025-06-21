import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    n = int(input())
    nc = n
    ncsum = 0
    while nc:
        ncsum += nc % 10
        nc = nc // 10
    if n % ncsum == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()