t=list(map(int,input().split()))
s=[t[i]*(2**(3-i)) for i in range(4)]
n=int(input())
p,d=divmod(n,2)
print(p*min(s)+d*min([i//2 for i in s[:3]]))