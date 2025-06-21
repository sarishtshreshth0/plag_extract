def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    n = int(input())
    c, s, f = [], [], []
    for i in range(n-1):
        ci, si, fi = map(int, input().split())
        c.append(ci)
        s.append(si)
        f.append(fi)
    ans = [0]*n
    
    for i in range(n-1):
        for j in range(i,n-1):
            ans[i] = max(ans[i]+(-ans[i]%f[j]), s[j])
            ans[i] += c[j]
    for x in ans:
        print(x)
        
            
                

             
            
        
    
if __name__ == '__main__':
    main()