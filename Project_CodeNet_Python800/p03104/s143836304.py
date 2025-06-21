a,b=map(int,input().split())
print((a*(a%2))^(b*(b%2==0))^(((b-a+(a%2==0 and b%2))//2)%2))