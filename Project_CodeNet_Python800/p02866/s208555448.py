def main():
    import sys
    input = sys.stdin.readline
    n = int(input())
    D = list(map(int,input().split()))
    mod = 998244353

    from collections import Counter

    node_cnt = Counter(D)
    set_d = sorted(list(set(D)))
    if D[0]!=0:
        print(0);exit()
    if set_d[-1]!=len(set_d)-1:
        print(0);exit()
    
    ans = 0
    pre = 1
    
    if 0 in node_cnt:
        if node_cnt[0]==1: 
            ans = 1
    for k,v in sorted(node_cnt.items()):
        ans*=pow(pre,v)
        ans%=mod
        pre = v
    print(ans)

if __name__=='__main__':
    main()