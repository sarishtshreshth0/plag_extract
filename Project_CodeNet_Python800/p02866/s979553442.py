from collections import Counter
 
mod = 998244353
 
def solve():
    N = int(input())
    Ds = list(map(int, input().split()))
    # 頂点1から頂点1は必ず深さ0
    if Ds[0] != 0:
        print(0)
        return
    
    counter = Counter(Ds)
    ret = 1
 
    if counter[0] > 1:
        print(0)
        return
    max_key = max(counter.keys())
    for i in range(1, max_key+1):
        if i not in counter:
            print(0)
            return
        
        ret = (ret*(counter[i-1]**counter[i]))%mod
        
    print(ret)
    
solve()
