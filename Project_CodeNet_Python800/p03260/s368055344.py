a,b = map(int,input().split())
print('YNeos'[a*b%2==0::2])