a,b=map(int,input().split())
A,B=a%2>0,b%2<1
print(a*A^((b-B-(a-1^A))//2%2)^b*B)