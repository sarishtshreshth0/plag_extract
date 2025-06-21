N, K = map(int,input().split())

def abc(n,m):
    a,b = divmod(n,m)
    return a,b

count = 0 
a = 1
while a !=0 :
    a,b = abc(N,K)

    N = a
    count += 1
print(count)    