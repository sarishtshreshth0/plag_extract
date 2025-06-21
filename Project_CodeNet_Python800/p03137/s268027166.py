n,m = map(int,input().split())
x = list(map(int,input().split()))
x.sort()
sa = [x[i+1]-x[i] for i in range(m-1)]
sa = sorted(sa)[::-1]
print(sum(sa[n-1:]))