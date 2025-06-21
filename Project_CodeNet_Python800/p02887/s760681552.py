def main():
    import sys
    readline = sys.stdin.buffer.readline

    n = int(readline())
    s = readline().rstrip().decode('utf-8')

    l = ''
    ans = 0
    for i in s:
        if i != l:
            l = i
            ans += 1 
    print(ans)

if __name__ == '__main__':
    main()