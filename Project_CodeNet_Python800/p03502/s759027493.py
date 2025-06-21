n = int(input())
n_ = n
s = 0 
while n_ > 0:
    r = n_%10
    s += r
    n_ = (n_-r)//10

print('Yes' if n%s==0 else 'No')
