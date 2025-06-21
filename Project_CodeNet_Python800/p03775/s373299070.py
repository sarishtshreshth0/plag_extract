def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    n = int(input())
    i = 1
    ans = 13
    while i*i <=n:
        if n%i == 0:
            tmp = max(len(str(i)), len(str(n//i)))
            ans = min(tmp, ans)
        i +=1 
    print(ans)
        
    
    
if __name__ == '__main__':
    main()