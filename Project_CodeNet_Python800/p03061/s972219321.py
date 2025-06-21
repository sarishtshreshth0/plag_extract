# https://atcoder.jp/contests/abc125/tasks/abc125_c

def main():
    import sys
    from fractions import gcd
    input = sys.stdin.readline

    def init(init_val):
        #set_val
        for i in range(n):
            seg[i+num-1]=init_val[i]    
        #built
        for i in range(num-2,-1,-1) :
            seg[i]=gcd(seg[2*i+1],seg[2*i+2]) 
        
    def update(k,x):
        k += num-1
        seg[k] = x
        while k:
            k = (k-1)//2
            seg[k] = gcd(seg[k*2+1],seg[k*2+2])
        
    def query(p,q):
        if q<=p:
            return ide_ele
        p += num-1
        q += num-2
        res=ide_ele
        while q-p>1:
            if p&1 == 0:
                res = gcd(res,seg[p])
            if q&1 == 1:
                res = gcd(res,seg[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        if p == q:
            res = gcd(res,seg[p])
        else:
            res = gcd(gcd(res,seg[p]),seg[q])
        return res

    n = int(input())
    a = tuple(map(int,input().split()))

    #####単位元######
    ide_ele = 0

    #num:n以上の最小の2のべき乗
    num =2**(n-1).bit_length()
    seg=[ide_ele]*2*num
    init(a)

    ans = -1
    for i in range(n):
        ans = max(ans,gcd(query(0,i),query(i+1,n)))
    print(ans)

if __name__ == '__main__':
    main()