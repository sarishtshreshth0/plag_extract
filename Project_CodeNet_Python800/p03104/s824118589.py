a,b=map(int,input().split())
a-=1
a_=[a,1,a+1,0]
b_=[b,1,b+1,0]
print(a_[a%4]^b_[b%4])