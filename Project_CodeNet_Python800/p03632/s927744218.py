a,b,c,d=map(int,input().split())
a_b=set(range(a,b+1))
c_d=set(range(c,d+1))
print(len(a_b&c_d)-1 if len(a_b&c_d)!=0  else 0)