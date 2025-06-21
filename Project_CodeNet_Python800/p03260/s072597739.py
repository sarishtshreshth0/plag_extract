A,B=map(int,input().split())
print('Yes' if ((A*B)%2==1 or (A*B*2)%2==1 or (A*B*3)%2==1) else 'No')