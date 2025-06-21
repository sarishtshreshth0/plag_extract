def baseConv(n,ro,ri=10):
    n = int(str(n),base=ri)
    s = ""
    nums = "0123456789abcdefghijklmnopqrstuvwxyz"
    while n:
        s += nums[n%ro]
        n //= ro
    return s[::-1]
  
n,k = map(int,input().split())
print(len(baseConv(n,k)))