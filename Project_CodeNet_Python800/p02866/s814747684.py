mod = 998244353

n = int(input())
D = list(map(int,input().split()))

if D[0] != 0:
    print(0)
else:
    nums = [0]*n
    for d in D:
        nums[d] += 1
    
    imp = False
    end = False
    
    if nums[0] > 1:
        imp = True
        
    for i in range(1,n):
        if nums[i] == 0:
            end = True
        else:
            if end:
                imp = True
                break
            
    if imp:
        print(0)
    else:
        ans = 1
        for i in range(1,n):
            if nums[i] == 0:
                break
            ans = ans*pow(nums[i-1], nums[i], mod)%mod
        print(ans)